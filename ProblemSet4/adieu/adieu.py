import sys, inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").title()

        if len(name) < 1:
            sys.exit(0)


        names.append(name)

    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(names)}")
        break