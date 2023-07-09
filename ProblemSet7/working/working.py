import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    first, second = s.split(" to ")
    hour1, olcek1 = first.split(" ")
    hour2, olcek2 = second.split(" ")

    minute1 = 0
    minute2 = 0

    if ":" in hour1:
        hour1, minute1 = hour1.split(":")
        minute1 = int(minute1)
        if not 0 <= minute1 < 60:
            raise ValueError

    if ":" in hour2:
        hour2, minute2 = hour2.split(":")
        minute2 = int(minute2)
        if not 0 <= minute2 < 60:
            raise ValueError


    hour1 = int(hour1)
    hour2 = int(hour2)





    if not 0 < hour1 < 13 or not 0 < hour2 < 13:
        raise ValueError



    if olcek1 == "PM":
        hour1 += 12

    if olcek2 == "PM":
        hour2 += 12

    if hour1 == 12:
        hour1 = 0

    if hour2 == 12:
        hour2 = 0

    if hour1 == 24:
        hour1 = 12

    if hour2 == 24:
        hour2 = 12

    if hour1 < 10:
        hour1 = str(hour1).zfill(2)

    if hour2 < 10:
        hour2 = str(hour2).zfill(2)

    if minute1 == 0:
        minute1 = str(minute1).zfill(2)

    if minute2 == 0:
        minute2 = str(minute2).zfill(2)

    return f"{hour1}:{str(minute1)} to {hour2}:{str(minute2)}"

if __name__ == "__main__":
    main()