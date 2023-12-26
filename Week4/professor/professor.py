import random
import sys

def main():
    getNumber = get_level()

    count = 1
    mark = 0
    for _ in range(10):
        x = generate_integer(getNumber)
        for _ in [0]:
            y = generate_integer(getNumber)

            result = x + y
            summ = input(f"{x} + {y} = ")
            if int(summ) == result:
                mark += 1

            while int(summ) != result:
                count += 1
                print("EEE")
                summ = input(f"{x} + {y} = ")
                if count >= 3:
                    print(result)
                    sys.exit("mark: " + str(mark))
    # print the score
    print("Score: " + str(mark))

# prompt for level
# reprompt
def get_level():
    input_level = input("Level: ")

    if input_level.isalpha() or int(input_level) <= 0 or int(input_level) > 3:
        input("Level: ")
    else:
        input_level = int(input_level)
        for i in [1,2,3]:
            if input_level == i:
                return input_level

# generate  level input
def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except:
        raise ValueError

if __name__ == "__main__":
    main()