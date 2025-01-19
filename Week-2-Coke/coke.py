PRICE_LEFT = 50
VALID_COIN = 25,10,5

def main():
    while True:
        question = int(input("Insert coin: "))

        #Checking that the coin inserted is acctually a coin we accept, if not we ask again
        if question not in VALID_COIN:
            print(f"Amount Due: {PRICE_LEFT}")
            # Continue to aske question
            continue

        else:

            # To use two funtions i have to break after calling function here
            if calculation(question):

                 # But i only want to break if I have 0 or less left.
                 # So I return True if i have less or == 0
                 break


def calculation(coin):
        # Global variables to use them from outside scope.
        global PRICE_LEFT
        global VALID_COIN

        PRICE_LEFT = PRICE_LEFT - coin
        if PRICE_LEFT > 0:
            print(f"Amount Due: {PRICE_LEFT}")

            # Return False to not break
            return False

        # Prints the change if we payed to much or the right amount.
        else:
            print(f"Change Owed: {abs(PRICE_LEFT)}")

            # Return True to break
            return True

main()

