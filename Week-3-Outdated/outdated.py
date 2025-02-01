def main():
    # full_date = input("Date: ")
    full_date = "9/8/1988"
    try:
        month, day, year = full_date.strip().split("/")
        print(month,day,year)
    except Exception:
        try:
            month, day, year = full_date.split(" ")
        except Exception as e:
            print(f"Error as {e}")
    
    formated_date = format_date(day, month, year)
    # TODO Format needs to be updated
    print(formated_date)



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
        print(f"Test 1")
        return year, month, day
    # Denne delen brukes hvis month er et tall
    else:
        print(f"Test 2")
        # For å itterere over liste av strings kan vi bruke i som int representasjon
        for i in range(len(months_of_the_year)):
            print(f"test 3 {i}")
            print(f"Month is {month}")
            # Siden input gir string er det viktig å sammenligne i med int av str month
            if i == int(month):
                print(f"Test 4{i}")
                print(f"Test 5: {year},{month}, {day}")
                return year, months_of_the_year[i], day
    

    
main()