'''
TODO
Design feedback from cs50 rubberduck ai:
To modularize the input_check function while keeping the input reprompting logic, 
you can separate the input validation and reprompting into different functions.
For example, you could have a function that checks if the input is valid and returns a boolean value. 
Then, in your main function, you can use a while loop to keep asking for input until the validation function returns true.
What do you think about this approach?
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
    day, month, year = check_input()

    fday, fmonth, fyear = format_output(day, month, year)
    print(f"{fyear}-{fmonth:02}-{fday:02}")


def check_input():

    # Since we need to reprompt all of this logic needs to be in one function.
    while True:

        date = input("Date: ")
        date = date.strip()

        # Logic for date entered with / seperator
        if ("/") in date:
            month, day, year = date.split("/")
            
        # Logic for date entered with space separator and a comma
        elif (",") in date:
            month, day, year = date.split()
            day = day.replace(",","")

            # Global list is titlecase.
            if month.title() in MONTHS_OF_THE_YEAR:
                month = find_month_int(month)
                
            else: 
                continue

        # All other formats results in reprompt from this line or line 45
        else:
            continue
        
        # We could assume all month had 31 days.
        try:

            if int(day) > 31 or int(month) > 12:
                continue
            else:
                break
        # Value error can be raised if month is placed in the wrong index of input string.
        except ValueError:
            continue

    return day, month, year

def format_output(day, month, year):

    # Formating done to print f string with 2 digits for month and day.
    day = int(day)
    month = int(month)
    year = int(year)

    return day, month, year


def find_month_int(month):
    global MONTHS_OF_THE_YEAR

    month = MONTHS_OF_THE_YEAR.index(month) 

    # Adding 1 makes sure we account for 0 indexed list
    return month +1 


# Probably not going to be a public lib, but good practice.
if __name__ == "__main__":
    main()
