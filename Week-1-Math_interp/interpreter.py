def main():
    string = input("Input: ").split()
    print(calculation(string))


def calculation(string):
    try:
        x = int(string[0])
        operator = string[1]
        y = int(string[2])
    except Exception as e:
        return f"Format error: {e}, Usecase: '1 + 2' remember the whitespace \N{slightly smiling face}"

    my_dict = {"+": lambda a,b : a + b,
               "-": lambda a,b : a - b,
               "*": lambda a,b : a * b,
               "/": lambda a,b : a / b}

    if operator in my_dict:
        return float(my_dict[operator](x,y))
    else:
        return "Error. Only these operators are valid '+', '-', '*', '/'"



main()
