import csv
import json
import requests


#genera un access token para utilizar en el proceso de extraccion.
def generate_access_token(user, password):
    authentication = "Basic ZWRnZWNsaTplZGdlY2xpc2VjcmV0" ##este valor es estatico para la edge api.
    url = "https://login.apigee.com/oauth/token"
    headers = {'Authorization': authentication, 'Accept': 'application/json;charset=utf-8', 'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    form_params = {'username': str(user),'password': str(password),'grant_type': 'password'}
    
    try:
        r = requests.post(url, data=form_params, headers=headers)
        if(r) and r.status_code == 200:
            print("Status Code: " + str(r.status_code) + ' - Operation: Token Generated')
            #print(json.dumps(r.json(), indent=4, sort_keys=True))
            return r.json()["access_token"]
        else:
            print("Status Code: " + str(r.status_code) + ' - Operation: Error')
            #print(json.dumps(r.json(), indent=4, sort_keys=True))
    except:
        print("Uknown Error")



#crea el csv con la data analitica estructurada
def create_analytics_csv(rows):
    header = ['organization','environment','apiproxy','transactions','time_range']
    with open('analytics.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        # write the header
        writer.writerow(header)
        
        # write the data
        writer.writerows(rows)


#Obtiene los datos asociados a organizacion y ambiente para extraer datos
def populate_org_details():
    with open('apigee_details.json') as fp:
        listObj = json.load(fp)
    return listObj['org'],listObj['environments'],listObj['user'],listObj['pass'], listObj['time_range']


#Extrae las analiticas de la organizacion segmentado por API
def extract_analytic_stats(org, env, dimension,token, time_range):
    url = "https://api.enterprise.apigee.com/v1/organizations/" + org + '/environments/' + env + "/stats/" + dimension
    headers = {'Authorization': 'Bearer ' + str(token) }
    params = {
        'select': 'sum(message_count)',
        'timeRange': str(time_range),
        'sortby': 'sum(message_count)',
        'sort': 'DESC'
    }


    try:
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            print("Status Code: " + str(r.status_code) + ' - Operation: Data fetched')
            #print(json.dumps(r.json(), indent=4, sort_keys=True))
            return r.json()
        else:
            print("Status Code: " + str(r.status_code) + ' - Operation: Error')
            #print(json.dumps(r.json(), indent=4, sort_keys=True))
    except:
        print("Uknown Error")


#Estructura la data para previo a la creacion del csv
def struct_data(data, org, env, time_range): 
    clean_list = []
    object_list = data["environments"][0]["dimensions"]
    for object in object_list:
        name = object["name"]
        count = object["metrics"][0]["values"][0]
        # header = ['organization','environment','apiproxy','transactions','time_range']
        clean_object = [org, env, name, count, time_range]
        clean_list.append(clean_object)
    return clean_list
        
