def main():
    print(calculation())


def calculation():
    # Try except to ensure int
    try:
        i = int(input("Kilograms: "))
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
    # E=mc^2 calculation
    return i*300_000_000**2

main()
