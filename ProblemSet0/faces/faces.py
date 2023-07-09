text = input()

def convert_to_emoji(text):

    emoji_dict = {
        ":)": "🙂",
        ":(": "🙁",
    }


    for key, value in emoji_dict.items():
        text = text.replace(key, value)
    return text

converted_text = convert_to_emoji(text)


print(converted_text)