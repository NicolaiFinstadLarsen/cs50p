def main():
    PRICE_LEFT = 50
    VALID_COIN = 25,10,5
    while True:
        question = int(input("Insert coin: "))
        if question not in VALID_COIN:
            print(f"Amount Due: {PRICE_LEFT}")
            continue

        PRICE_LEFT = PRICE_LEFT - question
        if PRICE_LEFT > 0:
            print(f"Amount Due: {PRICE_LEFT}")
            continue
        else:
            print(f"Change Owed: {abs(PRICE_LEFT)}")
            break


main()


# def main():
#     price_left = 50
#     valid_coin = {25,10,5}

#     while price_left > 0:

#         coin = int(input("Insert coin: "))

#         if coin in valid_coin:
#             price_left -= coin
#         else:
#             print(f"Amount Due {price_left}")

#         if price_left > 0:
#             print(f"Amount Due: {price_left}")
#         else:
#             print(f"Amount Owed {abs(price_left)}")
# main()

