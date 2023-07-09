
def camel_to_snake(camel):

    snake_case = ""
    for char in camel:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case



camel = input("camelCase: ").strip()


snake_case = camel_to_snake(camel)


print("snake_case = "+ snake_case)