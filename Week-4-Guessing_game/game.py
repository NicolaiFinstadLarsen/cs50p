import random
import sys


def main():
    while True:
        try:
            get_level = int(input("Level: "))
            if get_level < 1:
                continue
            break
        except ValueError:
            continue

    choose_number(get_level)


def choose_number(n):

    target = random.randint(1,n)

    while True:
        try:
            pick = int(input("Guess: "))
        except ValueError:
            continue

        if look_for_number(target, pick):
            sys.exit()


def look_for_number(target, pick):

    if pick == target:
        print("Just right!")
        return True
    elif pick > target:
        print("Too large!")
        return False
    else:
        print("Too small!")
        return False



main()
