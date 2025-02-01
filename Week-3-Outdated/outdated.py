'''
TODO
The printout format is the wrong way around.
There is no reprompt when incorrect input is given.
'''


def main():
    # full_date = input("Date: ").replace(",", "")
    # full_date = "9/8/1988"
    full_date = "september 8, 1988".replace(",", "")
    print(full_date)
    try:
        month, day, year = full_date.strip().split("/")
        print(month)
    except Exception:
        try:
            month, day, year = full_date.split(" ")
        except Exception as e:
            print(f"Error as {e}")

    # Strictly not nessessary with two lines, but more readable to me.
    fday, fmonth, fyear = format_date(day, month, year)
    print(f"{fyear}-{fmonth:02}-{fday:02}")



def format_date(day, month, year):
    months_of_the_year = [
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

    if month in months_of_the_year:
        count = 0
        # To itterate over over the list and compare with int we need a range.
        for i in months_of_the_year:
            print(f"test 3 i = {i}")
            print(f"Month is {month}")
            # Input returns a string, so I typecast to int.
            if i.title() == month:
                # print(f"Test 4{i}")
                print(f"Test 5: {year}-{count}-{day}")
                return year, count, day
            else:
                count += 1
        # print(f"Test 1")
            return year, month, day
    # This part is triggered if month is a number
    else:
        # TODO I am trying to compare the i in range of list of moths with the string month from input. Thats not how i saw it in my head.
        # print(f"Test 2 {year}-{month}-{day}")
        return day, month, year




main()
