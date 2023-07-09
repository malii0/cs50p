import sys, csv


def main():
    if valid_check(sys.argv):
        create(sys.argv[1], sys.argv[2])


def valid_check(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in argv[1]:
        sys.exit(f"Could not read {argv[1]}")

    return True


def create(input, output):
    try:
        with open(input) as csvfile:
            reader = csv.DictReader(csvfile)
            with open(output, "w", newline="") as new_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    name = row["name"].replace("\"", "").split(",")
                    writer.writerow({"first": name[1].strip(), "last": name[0].strip(), "house": row["house"].strip()})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()