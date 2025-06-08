import datetime
import inflect
import sys

def main():
    try:
        print("print0")
        user_input = get_input()
        print("print1")
        date1, date2 = format_input(user_input)
        print("print2")
    except Exception:
        sys.exit(1)
    if date1>date2:
         sys.exit(1)
    total_min_between = (datetime_daysbetween(date1, date2) * 24 * 60)
    #print(total_min_between)
    result = printing_result(total_min_between)
    print(f"{result} minutes")


def get_input():
        user_input = input("Date of Birth: ")
        return user_input


def format_input(user_input):
    # strptime(date_string, format)
    date1 = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
    date2 = datetime.date.today()
    # date2 = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d").date()
    return date1, date2


def datetime_daysbetween(date1, date2):
    return (date2 - date1).days


def printing_result(total_min_between):
    p = inflect.engine()
    result = p.number_to_words(total_min_between).capitalize().replace(" and", "")
    return result


if __name__=="__main__":
    main()
