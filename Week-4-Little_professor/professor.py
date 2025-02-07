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

def main():
    global correct_count
    global ROUNDS_OF_QUESTION
    error_count = 0
    
    x,y=get_level()

    while True:
        try:
            answer = int(input("Answer: "))
        except ValueError:
            continue

        # This whole wrong answer check should be in a separate func or loop so i can do three checks before moving on
        while True:
            if answer != x+y:
                print("EEE")
                error_count +=1
                # print(f"Error count: {error_count}")
                if error_count == 3:
                    print(f"{x} + {y} = {x+y}")
                    sys.exit(0)
                
                # print(f"Error count {error_count}")
                answer = int(input("Answer: "))

            elif answer == x+y:
                # print("correct")
                correct_count += 1
                if correct_count == ROUNDS_OF_QUESTION:
                    print(f"Score {correct_count-error_count}")
                break

        # Count to 3 to make it do next
        # Also do 10 qestions at a time
        if correct_count < ROUNDS_OF_QUESTION:
            x,y = get_level()
            continue
        else:
            sys.exit(0)
            

def get_level():
    global correct_count
    global level

    while True:
        if correct_count == 0:
            try:
                level = int(input("Level: "))
            except ValueError:
                continue

        if level in range(1,4):
            x, y = generate_integer(level)
            break
        else:
            continue
    return x,y


def generate_integer(level):

    
    x = random.randint(0,10**level-1)
    y = random.randint(0,10**level-1)

    print(f"{x} + {y}")
    return x,y

    
if __name__ == "__main__":
    main()