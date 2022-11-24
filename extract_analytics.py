from datetime import datetime
from functions import create_analytics_csv, extract_analytic_stats, populate_org_details, struct_data, generate_access_token
from cal import get_days_in_month_whole_year

#Orquesta el proceso de extraccion de informacion de Apigee
def main():
    org, environments, user, password, year, start_month, end_month, complete_year = populate_org_details()
    token = generate_access_token(user, password)
    dimension = "apiproxy"
    
    
    if complete_year is True:
        month_days = get_days_in_month_whole_year(year, 1, 12)
    else:
        month_days = get_days_in_month_whole_year(year, start_month, end_month)
    


    print("-------------Apigee Edge Extraction---------------")
    print("This process will fetch data using the following details:")
    print("Organization: " + org)
    print("Environments: " + str(environments))
    print("Starting extraction process...")
    start_time = datetime.now()
    result_list = []
    for month in month_days:
        if month < 9:
            time_range = "0{month}/0{from_day}/{year} 00:00~0{month}/{to_day}/{year} 23:59"
            time_range.format(month=month, from_day=1, year=year, to_day=month_days[str(month)])
        else:    
            time_range = "{month}/0{from_day}/{year} 00:00~{month}/{to_day}/{year} 23:59"
            time_range.format(month=month, from_day=1, year=year, to_day=month_days[str(month)])
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

