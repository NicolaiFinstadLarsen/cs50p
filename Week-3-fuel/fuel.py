def main():
    result = (get_fuel())
    if result:
        print(result)
    else:
        return


def get_fuel():
    try:
        x, y = input("Fuel: ").split("/")
    except ValueError:
        main()
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        #print(f"Error message: Usage 'x/y' \nError: {e}")
        main()
    else:
        # This return is ugly
        try:
            return return_value(x / y * 100)
        except ZeroDivisionError as e:
            #print(f"Error message: You can not divide by 0 \nError: {e}")
            main()


def return_value(num):
    if num > 100:
        main()
    if num >= 99:
        return "F"
    elif num <= 1:
        return "E"
    else:
        return (f"{num:.0f}%")


main()
