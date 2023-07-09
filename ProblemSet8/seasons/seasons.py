import sys
import inflect
from datetime import date, datetime

p = inflect.engine()

def main():
    birthDate = input("Date of Birth: ")
    validDate = date_validate(birthDate)
    days_difference = calc_difference(validDate)
    print(add_text(days_difference))

def date_validate(birthDate):
    try:
        input = date.fromisoformat(birthDate)
        return input
    except ValueError:
        sys.exit("Invalid date")


def calc_difference(days):
    today = date.today()
    daysDiff = today - days
    return daysDiff.days * 24 * 60

def add_text(text):
    text = p.number_to_words(text, andword="")
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()