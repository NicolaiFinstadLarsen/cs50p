full_dict = {}

def main():
    while True:
        try:
            item = input("Item : ").strip()
            shopping = add_to_list(item)
        except (EOFError, KeyboardInterrupt):
            print(shopping)
            break
    return

def add_to_list(item):
    global full_dict
    if item in full_dict:
        full_dict[item] += 1
    else:
        full_dict[item] = 1

    

main()