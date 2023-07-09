import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        errors = 0
        x = int(generate_integer(level))
        y = int(generate_integer(level))
        solution = int(x+y)
        while errors < 3:
            answer = int(input(f"{x} + {y} = "))
            if answer == solution:
                break
            else:
                print("EEE")
                errors += 1
                if errors == 3:
                     print(f"{x} + {y} = {solution}")
                continue
        if errors == 0:
             score += 1
    print(f"Score: {score}")

def get_level():
    level = 0
    while True:
        try:
            level = int(input("Level: "))
            if 0 >= level or level > 3:
                raise ValueError
            break
        except ValueError:
            continue
    return level


def generate_integer(level):
        match level:
             case 1:
                  number = random.randint(0,9)
                  return number
             case 2:
                  number = random.randint(10,99)
                  return number
             case 3:
                  number = random.randint(100,999)
                  return number


if __name__ == "__main__":
    main()