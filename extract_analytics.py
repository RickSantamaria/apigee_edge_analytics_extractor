from datetime import datetime
from functions import create_analytics_csv, extract_analytic_stats, populate_org_details, struct_data, generate_access_token


#Orquesta el proceso de extraccion de informacion de Apigee
def main():
    org, environments, user, password, time_range = populate_org_details()
    token = generate_access_token(user, password)
    dimension = "apiproxy"
    
    print("-------------Apigee Edge Extraction---------------")
    print("This process will fetch data using the following details:")
    print("Organization: " + org)
    print("Environments: " + str(environments))
    print("Starting extraction process...")
    start_time = datetime.now()
    result_list = []
    for env in environments:
        result = extract_analytic_stats(org, env, dimension, token, time_range)
        structured_data = struct_data(result, org, env, time_range)
        result_list.extend(structured_data)
        print("Ended " + env + " environment extraction")

    create_analytics_csv(result_list)
    print("Ended " + org + " organization extraction.")
    print("Extraction Elapsed Time:  %s" % (datetime.now() - start_time))


if __name__ == "__main__":
    main()

