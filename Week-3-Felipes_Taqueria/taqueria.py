def main():
    total = 0
    while True:
        try:
            choice = input("Item: ").strip().title()
            price = get_price(choice)
            if price is not None:
                total += price
                #print(f"Added {choice}: ${price:.2f}, Total: ${total:.2f}")
                print(f"${total:.2f}")
        except (EOFError, KeyboardInterrupt):
            print(f"${total:.2f}")
            break


def get_price(pick):
    food = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    return food.get(pick)

if __name__ == "__main__":
    main()
