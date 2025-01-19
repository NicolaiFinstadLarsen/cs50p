# def main():
#     # Yeah I'm tired, I'll revisit later....
#     string = input("string: ").strip()
#     string = string.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
#     string = string.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","")
#     print(string)



# main()

def main():
    #vowels = "a","A","e","E","i","I","o","O","u","U"
    vowels = "a","e","i","o","u"
    string = input("String: ")
    new_string = ""
    for c in string:
        if c.lower() in vowels:
            continue
        else:
            new_string = new_string + c
    print(new_string)
main()
