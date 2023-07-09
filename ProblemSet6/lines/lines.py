import sys


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")


if ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")

total_lines  = 0

for l in file.read().splitlines():
    if len(l.strip()) == 0:
        continue

    if not l.strip().startswith("#"):
        total_lines += 1

print(total_lines)

