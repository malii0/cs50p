import random
while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
                raise ValueError
        break
    except ValueError:
         continue
number = random.randint(1,level)
guess = 0
while guess != number:
        try:
            guess = int(input("Guess: "))
            if guess == number:
                print("Just Right!")
                break
            elif guess < number:
                print("Too small!")
            else:
                print("Too Large!")
        except ValueError:
            continue

