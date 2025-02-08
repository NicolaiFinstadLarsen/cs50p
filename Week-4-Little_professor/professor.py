'''
TODO
Code cleanup, alot of uneeded code right now.
Get closer to pset spec with:¨
Making 10 questions in a list right away mabye?
Remove ValueError checks in get_level?
Raise ValueError if level is not correct in gen int func instead?
'''

import random
import sys

correct_count = 0
level = 0
ROUNDS_OF_QUESTION = 10
CORRECT_LEVELS = [1,2,3]

def main():
    formated_level = get_level()
    generate_integer(formated_level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in CORRECT_LEVELS:
                continue
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    global correct_count
    while True:
        tries = 0
        for i in range(ROUNDS_OF_QUESTION):
            x = random.randint(10**level/10, 10**level-1)
            y = random.randint(10**level/10, 10**level-1)
            print(f"{x} + {y} = ")
            while True:
                try:
                    answer = int(input())
                except ValueError:
                    continue
                if answer == x+y:
                    correct_count += 1
                    break
                else:
                    print("EEE")
                    tries += 1
                if tries == 3:
                    print(f"{x} + {y} = {x+y}")
                    sys.exit()
                else:
                    continue
        print(f"Score: {correct_count-tries}")
        break
                





    
if __name__ == "__main__":
    main()