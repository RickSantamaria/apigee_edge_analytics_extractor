import calendar

def get_days_in_month(year, month):
    return(calendar.monthrange(year, month)[1])


def get_days_in_month_whole_year(year, start_month, end_month):
    day_in_months_list = {}
    for month in range(start_month, end_month + 1):
        day_in_months_list[str(month)] = calendar.monthrange(year, month)[1]
    print(day_in_months_list)
    

if __name__ == "__main__":
    get_days_in_month_whole_year(2023)

