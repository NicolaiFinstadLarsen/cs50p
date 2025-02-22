import sys

def main():
    # While loop is the best way to repomp the user for input.
    while True:
        try:
            gas = input("Fuel: ") # Had to put the input in main
            percent = int(convert(gas))
            # print(percent)
            if percent in range(0, 101):
                break
        except (ValueError, ZeroDivisionError):
            continue
    result = gauge(percent)

    if result:
        print(result)
    else:
        return


def convert(fraction):
    x, y = fraction.split("/") # Split it here. For the assert to work how i wanted. I wanted the convert to only take one positional argument
    try:
        x = int(x)
        y = int(y)

    # We raise the error and catch it in main to also be able to assert it in the pytest.
    except ValueError:
        raise ValueError # If X and/or Y is not an integer,
    if y != 0:
        if x > y:
            raise ValueError # or if X is greater than Y, then convert should raise a ValueError

    # This return is ugly
    try:
        # print(int((x/y)*100))
        number = int(x / y * 100) # Pset spec wanted me to return just an int here
        # print(type(number))
        return number
    except ZeroDivisionError:
        raise ZeroDivisionError



def gauge(percentage):
    if percentage > 100:
        return
    if percentage < 0:
        return
    if percentage == 99 or percentage == 100:
        return "F"
    elif percentage == 0 or percentage == 1:
        return "E"
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()
