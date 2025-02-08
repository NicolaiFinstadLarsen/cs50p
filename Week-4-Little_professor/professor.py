import random

ROUNDS_OF_QUESTION = 10
CORRECT_LEVELS = [1,2,3]

def main():
    formated_level = get_level()
    numbers = generate_integer(formated_level)
    score = run_answer(numbers)
    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in CORRECT_LEVELS:
                return level    
        except ValueError:
            continue


def generate_integer(level):
    # This is so ugly, but since check50 wants the questions in a list. This is how i managed to do that.
    # My code without a list is much prettier.
    # Im also proud over my order of magnitude solution to the n digits!
    question = [(random.randint(10**(level-1), 10**level - 1),
                 random.randint(10**(level-1), 10**level - 1)) 
                 for i in range(ROUNDS_OF_QUESTION)]
    
    return question


def run_answer(numbers):

    # I look like i need to have this in another func when running check 50...
    correct_count = 0

    for x, y in numbers:
        tries = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x+y:
                    correct_count += 1
                    break
                else:
                    print("EEE")
                    
            except ValueError:
                continue

            tries += 1

            if tries == 3:
                print(f"{x} + {y} = {x+y}")
                break
            else:
                continue

    return correct_count


    
if __name__ == "__main__":
    main()