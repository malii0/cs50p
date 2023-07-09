def main():
    s: str = input("Fraction: ")
    try:


        percent = convert(s)



    except Exception:
        main()

if __name__ == "__main__":
    main()



def convert(fraction):
    _split = fraction.split("/")
    x: int = int(_split[0])
    y: int = int(_split[1])

    if x > y or y == 0:
        raise Exception("Invalid x or y values")

    return int(round((x/y)*100))


def gauge(percentage):
    if percentage <= 1:
            return "E"

    elif percentage >= 99:
            return "F"

    else:
            return f"{percentage}%"