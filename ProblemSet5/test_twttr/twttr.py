def main():
    input = input("Enter a word: ")
output = shorten(input)
print("Output:", output)


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()