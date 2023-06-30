def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar, number = d.split("$")
    number = round(float(number), 1)
    return number



def percent_to_float(p):
    number, percent = p.split("%")
    number = float(number)/100
    return number

main()