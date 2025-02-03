'''
TODO
Gettin the comparison of moth and list to work.
There is no reprompt when incorrect input is given.
'''
MONTHS_OF_THE_YEAR = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]


def main():
    global MONTHS_OF_THE_YEAR
    full_date = input("Date: ").replace(",", "").replace("/"," ").split(" ") #Why not?
    # full_date = "9/8/1988".replace(",", "").replace("/"," ").split(" ").strip() #Why not?
    # full_date = "september 8, 1988".replace(",", "").replace("/"," ").split(" ").strip() #Why not?
    while True:
        try:
            month, day, year = full_date
            break
        except Exception:
                main()
    # This was the missing piece! 
    month = month.title()
    
    #print(f"Month after the split in to 3 variables: {month}")

    fday, fmonth, fyear = format_date(day, month, year)
    if fday == None or fmonth == None or fyear == None:
        main()


    print(f"{fyear}-{fmonth:02}-{fday:02}")


def find_month_int(month):
    global MONTHS_OF_THE_YEAR
    for i in range(12):
        # print(f"Value of i = {i}")
        # print(f"Month of year index i = {MONTHS_OF_THE_YEAR[i]}")
        # Looks like the == does not work as expected here..
        # 
        if month == MONTHS_OF_THE_YEAR[i]:
            print(f"Return value: {i+1}")
            return i + 1


def format_date(day, month, year):
    print(f"Format_date day: {day}")
    print(f"Format_date month: {month}")
    try:
        fday = int(day)
    except ValueError:
        return
    try:
        fmonth = int(month)
    except ValueError:
        # So we do trigger the exception.
        # Then is should be in the find_month_int function
        # print(f"ValueError: {month}")
        month_by_int = find_month_int(month)
        # print(f"After function call: {month_by_int}")
        fmonth = month_by_int
    fyear = int(year)

    return fday, fmonth, fyear

main()
