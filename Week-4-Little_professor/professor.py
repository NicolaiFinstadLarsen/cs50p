import random
import sys


def main():
    count = 0
    error_count = 0
    x,y=get_level()
    while True:
        try:
            answer = int(input("Answer: "))
        except ValueError:
            continue
        # This whole wrong answer check should be in a separate func or loop so i can do three checks before moving on
        if answer != x+y:
            print("EEE")
            answer = int(input("Answer: "))
            error_count +=1
            continue
        if error_count == 3:
            sys.exit(0)
        elif answer == x+y:
            print("correct")

        # Count to 3 to make it do next
        # Also do 10 qestions at a time
        if count < 10:
            x,y = get_level()
            continue
        else:
            sys.exit(0)
            

def get_level():
    while True:
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