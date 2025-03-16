import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"((\d+)(:(\d+))?)? (AM|PM) to ((\d+)(:(\d+))?)? (AM|PM)", s):
        first_num = match.group(1)
        second_num = match.group(6)
        first_day = match.group(5)
        second_day = match.group(10)

        # Initial ValueError check if hour is out of time.
        # I guess i could have had the minute check here as well..
        if int(match.group(2)) > 12 or int(match.group(7)) > 12:
            raise ValueError

        # PM handeling
        if "PM" in first_day and "12" not in match.group(2):
            if ":" in first_num:
                hour, minute = first_num.split(":")
                temp_hour = int(hour)+12
                hour = str(temp_hour)
                first_num = hour+":"+minute

                if int(minute) > 59:
                    raise ValueError
            elif ":" not in first_num:
                hour = int(first_num) + 12
                first_num = str(hour)+":"+"00"

        if "PM" in second_day and "12" not in match.group(7):
            if ":" in second_num:
                hour, minute = second_num.split(":")
                temp_hour = int(hour)+12
                hour = str(temp_hour)
                second_num = hour+":"+minute

                if int(minute) > 59:
                    raise ValueError

            elif ":" not in second_num:
                hour = int(second_num) + 12
                second_num = str(hour)+":"+"00"


        # AM handeling
        if "AM" in first_day and "12" not in match.group(2):
            if ":" in first_num:
                hour, minute = first_num.split(":")
                temp_hour = int(hour)
                hour = str(temp_hour)
                first_num = "0"+hour+":"+minute

                if int(hour) > 12 or int(minute) > 59:
                    raise ValueError
            elif ":" not in first_num:
                hour = int(first_num)
                first_num = "0"+str(hour)+":"+"00"

        if "AM" in second_day and "12" not in match.group(7):
            if ":" in second_num:
                hour, minute = second_num.split(":")
                temp_hour = int(hour)
                hour = str(temp_hour)
                second_num = "0"+hour+":"+minute

                if int(hour) > 12 or int(minute) > 59:
                    raise ValueError

            elif ":" not in second_num:
                hour = int(second_num)
                second_num = "0"+str(hour)+":"+"00"



        # AM and 12 handeling
        if "AM" in first_day and "12" in match.group(2):
            if ":" in first_num:
                hour, minute = first_num.split(":")
                hour = "00"
                first_num = hour+":"+minute

                if int(hour) > 12 or int(minute) > 59:
                    raise ValueError
            elif ":" not in first_num:
                hour = "00"
                first_num = str(hour)+":"+"00"

        if "AM" in second_day and "12" in match.group(7):
            if ":" in second_num:
                hour, minute = second_num.split(":")
                hour = "00"
                second_num = hour+":"+minute

                if int(hour) > 12 or int(minute) > 59:
                    raise ValueError

            elif ":" not in second_num:
                hour = "00"
                second_num = hour+":"+"00"


        # PM and 12 handeling
        if "PM" in first_day and "12" in match.group(2):
            if ":" in first_num:
                hour, minute = first_num.split(":")
                hour = "12"
                first_num = hour+":"+minute

                if int(hour) > 12 or int(minute) > 59:
                    raise ValueError
            elif ":" not in first_num:
                hour = "12"
                first_num = str(hour)+":"+"00"

        if "PM" in second_day and "12" in match.group(7):
            if ":" in second_num:
                hour, minute = second_num.split(":")
                hour = "12"
                second_num = hour+":"+minute

                if int(hour) > 12 or int(minute) > 59:
                    raise ValueError

            elif ":" not in second_num:
                hour = "12"
                second_num = hour+":"+"00"

        return f"{first_num} to {second_num}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
