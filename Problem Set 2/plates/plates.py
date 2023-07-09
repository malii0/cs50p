def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def check_first_two_letters(word):
    if len(word) >= 2 and word[0].isalpha() and word[1].isalpha():
        return True

    else:
        return False

def check_min_max(word):
    if 2 <= len(word) <= 6:
        return True
    else:
        return False

def check_middle_number(s):
    first_num = len(s)-1
    for character in s:
        if character.isnumeric():
            if character=='0':
                return False
            first_num = s.index(character)
            break
    for character in s:
        if s.index(character)<= first_num:
            pass
        else:
            if character.isalpha():
                return False

    return True

def check_no(word):

    punctuation_marks = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    for char in word:
        if char in punctuation_marks:
            return False
    return True


def is_valid(s):

    if check_first_two_letters(s) and check_min_max(s) and check_no(s) and check_middle_number(s):
        return True
    else:
        return False

main()