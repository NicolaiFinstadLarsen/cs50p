# global variable ensures its in scope for all functions
FULL_SHOPPING_DICT = {}

def main():
    global FULL_SHOPPING_DICT
    while True:
        try:
            item = input("Item : ").strip().lower()
            add_to_list(item)
            # print(FULL_SHOPPING_DICT)
        # KeyboardInterrupt is not for cs50, but for my local VScode. Since the EOFError did not work...
        except (EOFError, KeyboardInterrupt):
            # new line before we print the list for aestetics
            print()
            # using .items to get both key and value, since without it will only return key.
            # This is cool. We can use "sorted(dict.items())" to sort by key and itterate both key and value
            for item, numbers in  sorted(FULL_SHOPPING_DICT.items()):
                # Upper for the pset spec
                print(numbers, item.upper())
            break
                

def add_to_list(item):
    global FULL_SHOPPING_DICT
    if item in FULL_SHOPPING_DICT:
        # Remember, to modify dicts we use [], not {}.
        FULL_SHOPPING_DICT[item] += 1
        return FULL_SHOPPING_DICT
    else:
        FULL_SHOPPING_DICT[item] = 1
        return FULL_SHOPPING_DICT

    
main()