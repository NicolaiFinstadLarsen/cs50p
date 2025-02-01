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
    full_date = input("Date: ").replace(",", "").replace("/"," ").split(" ")
    # full_date = "9/8/1988".replace(",", "").replace("/"," ").split(" ")
    # full_date = "september 8, 1988".replace(",", "").replace("/"," ").split(" ")

    month, day, year = full_date
    # This was the missing piece! 
    month = month.title()
    # print(f"Month after the split in to 3 variables: {month}")

    fday, fmonth, fyear = format_date(day, month, year)

    print(f"{fyear}-{fmonth:02}-{fday:02}")


def find_month_int(month):
    global MONTHS_OF_THE_YEAR
    for i in range(12):
        # print(f"Value of i = {i}")
        # print(f"Month of year index i = {MONTHS_OF_THE_YEAR[i]}")
        # Looks like the == does not work as expected here..
        # 
        if month == MONTHS_OF_THE_YEAR[i]:
            # print(f"Return value: {i+1}")
            return i + 1




def format_date(day, month, year):
    '''
    I can do some of the main function in this fuction.
    To much is happening i main at the moment
    '''
    try:
        fday = int(day)
    # TODO reprompt for wrong input...
    except ValueError:
        main()
    try:
        fmonth = int(month)
    except ValueError:
        # So we do trigger the exception.
        # Then is should be in the find_month_int function
        # print(f"ValueError: {month}")
        month_by_int = find_month_int(month)
        # print(f"After function call: {month_by_int}")
        fmonth = month_by_int
    # fmonth is none here. What happened?
    fyear = int(year)

    return fday, fmonth, fyear

main()
