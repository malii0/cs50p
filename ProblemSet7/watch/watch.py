
import re

def main():
    html: str = input("HTML: ").strip()
    print(parse(html))

def parse(s: str):
    try:
        url: re.Match[str] = re.search('(?<=embed\/).*?(?=")', s)
        return f"https://youtu.be/{url.group(0)}"
    except Exception:
        return None

if __name__ == "__main__":
    main()

