def main():
    s = input("Greeting: ").lower().strip()
    print(greet(s))


def greet(st):
    if st.startswith("hello"):
        return "$0"
    elif st.startswith("h"):
        return "$20"
    else:
        return "$100"


main()
