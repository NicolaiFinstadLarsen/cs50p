def main():
    word = input("String: ")

    print(shorten(word))


def shorten(word):
    vowels = "a","e","i","o","u"
    
    new_string = ""
    for c in word:
        if c.lower() in vowels:
            continue
        else:
            new_string = new_string + c
    return new_string


if __name__ == "__main__":
    main()