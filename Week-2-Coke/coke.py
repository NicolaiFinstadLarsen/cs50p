def main():
    PRICE_LEFT = 50
    VALID_COIN = 25,10,5
    while True:
        question = int(input("Insert coin: "))
        if question not in VALID_COIN:
            print("Amount Due:", PRICE_LEFT)
            continue

        PRICE_LEFT = PRICE_LEFT - question
        if PRICE_LEFT > 0:
            print("Amount Due:", PRICE_LEFT)
            continue
        else:
            print("Change Owed:", abs(PRICE_LEFT))
            break


main()