while True:
    date = input("Enter the date (DD-MM-YYYY): ")
    test = date
    if len(test) == 10 and test[2] == "-" and test[5] == "-": 
        day = int(test[0:2])
        month = int(test[3:5])
        year = int(test[6:10])
        check_year = year > 1900 and year <= 2022
        check_month = month >= 1 and month <= 12
        check_day_31 = day <= 31 and (month in [1,3,5,7,8,10,12])
        check_day_30 = day <= 30 and (month in [4,6,9,11])
        check_day_Feb = month == 2 and ((day <= 29 and year %4 == 0) or day <= 28)
        if check_year:
            if check_month: 
                if check_day_31 or check_day_30 or check_day_Feb:
                    break 
                else:
                    print("Error in day")
            else:
                print("Error in year")
        else:
            print("Error in month")
    else:
        print("Error in format")
print("Date accepted")



