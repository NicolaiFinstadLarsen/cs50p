def main():
    greeting = input("Greeting: ").lower().strip()
    print(value(greeting))


def value(greeting):
    greeting = greeting.lower().strip() # Line taken from main to greet for PyTest reasons
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
