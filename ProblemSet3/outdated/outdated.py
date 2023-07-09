months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    try:
        date = input("Date: ")
        if date[0].isalpha():
            if "/" in date or ", "not in date :
                pass
            else:
                m, d , y = date.replace("," , "").split(" ")

                if 0 < int(d) < 32:
                    if m in months:
                        for i in range(len(months)):
                            if m == months[i]:
                                m = i + 1
                    print(f"{y}-{int(m):02}-{int(d):02}")
                    break
        elif not date[0].isalpha():
            if "," in date or "/" not in date:
                pass
            else:
                m, d , y = date.split("/")
                if 0 < int(d) < 32 and 0 < int(m) < 13:
                    print(f"{int(y)}-{int(m):02}-{int(d):02}")
                    break
                else:
                    pass
    except EOFError:
        break

