def main():
    # I will not add error handeling since the pset states the input will have this format
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # dollars = dollars_to_float("$50.00")
    # percent = percent_to_float("15%")
    tip = dollars * percent
    print(f"Dollars = {dollars} and percent = {percent}")
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.replace("$", ""))
    return d


def percent_to_float(p):
    p = float(p.replace("%", ""))
    return p/100


main()
