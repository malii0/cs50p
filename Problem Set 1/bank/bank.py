greeting = input("Greeting: ").strip()

greeting = greeting.lower()

if greeting.startswith("h"):
    if greeting.startswith("hello"):
        print("$0")
    else:
        print("$20")

else:
    print("$100")