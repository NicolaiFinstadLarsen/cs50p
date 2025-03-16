from validator_collection import validators

def main():
    print(validation(input("Email: ")))

def validation(s):
    try:
        s = validators.email(s)
        return "Valid"
    except ValueError:
        return "Invalid"
    
if __name__ == "__main__":
    main()