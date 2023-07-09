import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE)
    return len(count)

...


if __name__ == "__main__":
    main()