def main():
    #string = "firstName"
    string = input("CamelCase: ")
    print(convert_camel_to_snake(string))

def convert_camel_to_snake(s):
    # Making a new list so that we dont itterate over the same list we make changes to.
    new_list = list(s)
    count = 0

    for x in s:
        count += 1
        if x.isupper():
            new_list.insert(count - 1, "_")
            # Since we add an element to list we should add one to count aswell.
            count += 1

    # str(new_list).lower() gives me a list where each element is a string in lowercase.
    # This gives me a string.
    # Its an empty string that i join with new_list
    s = "".join(new_list).lower()
    return s


main()
