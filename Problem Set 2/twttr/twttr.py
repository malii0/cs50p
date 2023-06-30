
def remove_vowels(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result



input = input("Enter a word: ")
output = remove_vowels(input)
print("Output:", output)
