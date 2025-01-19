def main():
    string = input("CamelCase: ").strip()
    print(convert_camel_to_snake(string))


def convert_camel_to_snake(s):
    """
    Convert a CamelCase string to snake_case.
    """
    return "".join(["_" + char.lower() if char.isupper() else char for char in s]).lstrip("_")


if __name__ == "__main__":
    main()