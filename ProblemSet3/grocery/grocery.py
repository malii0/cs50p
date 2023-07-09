
groceries: dict[str, int] = {}

while True:
    try:

        item: str = input()

        if item not in groceries:
            groceries[item] = 0

        groceries[item] += 1
    except EOFError:
        count:  list[str] = list(groceries.keys())
        count.sort()
        for c in count:
            print(f"{groceries[c]} {c.upper()}")
            
        break

