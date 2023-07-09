import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):

    try:
        ip = ip.split(".")

        if 4 < len(ip) or len(ip) < 4:
            return False

        for i in ip:
            if int(i) > 255:
                return False


    except ValueError:
        return False

    return True


if __name__ == "__main__":
    main()