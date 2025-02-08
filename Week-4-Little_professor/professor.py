import random

# Using const to remove magic numbers, and for easier changing of variable
ROUNDS_OF_QUESTION = 10
CORRECT_LEVELS = [1, 2, 3]


def main():
    formated_level = get_level()
    numbers = generate_integer(formated_level)
    score = run_answer(numbers)
    print(score)


def get_level():
    # Getting level from user, while checking if its a good input.
    while True:
        try:
            level = int(input("Level: "))
            if level in CORRECT_LEVELS:
                return level
        except ValueError:
            continue


def generate_integer(level):
    '''
    Im proud over my order of magnitude solution to the n digits!
    Unfortunatly the check50 does not like it. So i cant use it for the submit :(
    I dont know why check 50 want me to have the nums in a list.
    It took so much more work.
    '''

    # Initialize the list before the itteration.
    numbers = []
    for i in range(ROUNDS_OF_QUESTION):

        # x = random.randint(10**(level-1), 10**level - 1)
        # y = random.randint(10**(level-1), 10**level - 1)

        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        if level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        if level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        # Get it all in one list by extending numbers with both x and y every itteration.
        numbers.extend([x, y])

    # print(numbers)
    return numbers


def run_answer(numbers):
    '''
    I look like i need to have this in another func when running check 50...
    The check50 did not like the print statements in the same func as the list building of questions
    '''

    correct_count = 0

    # Divide the list to two variables by using two step argument
    # Since we use step two we dont need len(numbers)-1
    for i in range(0, len(numbers)-1, 2):
        x, y = numbers[i], numbers[i+1]

        # Looping thru until either correct answer or tries == 3 aka. three missed guesses from user.
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

            # Three missed guesses gives answer and goes on to next question
            if tries == 3:
                print(f"{x} + {y} = {x+y}")
                break
            else:
                continue

    return correct_count


if __name__ == "__main__":
    main()
