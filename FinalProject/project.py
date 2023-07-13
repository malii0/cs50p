import random
import string

def main():


    select_menu()


def menu():
    print("\n")
    print("================")
    print("Password Manager")
    print("================")
    print("[1] List saved passwords")
    print("[2] Save new password")
    print("[3] Generate new password")
    print("[4] Quit Program")
    print("================")


def save_p():

    name = input("What is your password name?: ")
    password = input("What is your password? (If you want to generate new one type 'g'): ")

    if password == "g":
        password = give_generated()
        print("Generated Password: ", password)
    with open("passwords.txt", "a") as file:
        file.write(f"{name} - {password}\n")
    print('\n \n\u001b[3m' + 'New Password Saved' + '\u001b[0m \n \n')


def select_menu():
    while True:
        try:
            data  = []
            with open('passwords.txt', 'r', encoding='utf-8') as file:
                for  line in file:
                    data.append(f"{line.rstrip()} \n")
            menu()
            option = int(input("Select the option you want to do: "))

            if option == 1:

                select_menu2(data)

            elif option == 2:

                save_p()

            elif option == 3:

                print(f"\nGenerated Password: {give_generated()}")

            elif option == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid option ")
        except EOFError:
            break


def select_menu2(data):
    if data:
        while True:
            try:
                print("\n")
                print("================")
                print("Saved Passwords")
                print("================")
                for password in get_passwords():
                    print(password)
                print("================")
                print("[1] Edit Passwords")
                print("[2] Delete Passwords")
                print("[3] Back to Menu")
                print("================")
                option2 = int(input("Select the option you want to do: "))

                if option2 == 1:
                    edit_menu(data)

                elif option2 == 2:
                    if delete_menu(data) == True:
                        break

                elif option2 == 3:
                    break
                else:
                    raise ValueError
            except ValueError or EOFError:
                print("Invalid option ")
    else:
        print("\n")
        print("There are no saved passwords. ")


def give_generated():

    while True:
        spec_c = input("Do you want a special character in the password? [Y(y)/N(n)]: ")

        if spec_c.strip() == "Y" or spec_c.strip() == "y":
            length = int(input("Enter the password length: "))


            if 129 > length and length > 4:
                a = "!@#$%^*_./&"
                characters = string.ascii_letters + string.digits + a
                while True:
                    password = ''.join(random.choice(characters) for _ in range(length))
                    if (any(c.isdigit() for c in password) and
                        any(c.islower() for c in password) and
                        any(c.isupper() for c in password) and
                        any(c in a for c in password)):
                        return password
            else:
                print("Password length must be between 5 and 128. ")




        elif spec_c.strip() == "N" or spec_c.strip() == "n":
            length = int(input("Enter the password length: "))
            if 129 > length and length > 4:
                characters = string.ascii_letters + string.digits
                while True:
                    password = ''.join(random.choice(characters) for _ in range(length))
                    if (any(c.isdigit() for c in password) and
                        any(c.islower() for c in password) and
                        any(c.isupper() for c in password)):
                        return password
            else:
                print("Password length must be between 5 and 128. ")


        else:
            print("Invalid Option")
            continue



def get_passwords():
    passwords = []
    with open("passwords.txt") as file:
        for i, line in enumerate(file, start=1):
            passwords.append(f"{i} {line.rstrip()} ")

    return passwords


def edit_menu(data):
    print("\n")
    print("================")
    print("Edit Password")
    print("================")
    for password in get_passwords():
        print(password)
    print("================")

    while True:
        try:
            line = input("Enter the line number of the password you want to edit: ")

            if not line.isdigit():
                print("Invalid line")
                continue

            line_num = int(line)
            if line_num < 1 or line_num > len(data):
                print("Invalid line")
                continue

            password = input("What is your new password? (If you want to generate a new one, type 'g'): ")
            name = data[line_num - 1].split(" -")[0]
            data[line_num - 1] = f"{name} - {password}\n"

            with open('passwords.txt', 'w', encoding='utf-8') as file:
                for i in data:
                    file.write(f"{i}")

            break

        except ValueError:
            print("Invalid line")
            continue
        except EOFError:
            break

    print('\n \n\u001b[3m' + 'Password Edited' + '\u001b[0m \n \n')


def delete_menu(data):
            print("\n")
            print("================")
            print("Delete Password")
            print("================")
            for password in get_passwords():
                    print(password)
            print("================")

            while True:
                try:
                    line = int(input("Enter the number of the line you want to delete (If you want to delete all, type '0'): "))

                    if line < 0 or line > len(data):
                        print("Invalid line")
                        raise ValueError

                    elif line == 0:
                        data.clear()
                        with open('passwords.txt', 'w', encoding='utf-8') as file:
                            for i in data:
                                file.writelines(f"{i}")
                        print('\n \n\u001b[3m' + 'All Saved Passwords Deleted' + '\u001b[0m \n \n')
                        return True

                    else:
                        del data[line-1]
                        with open('passwords.txt', 'w', encoding='utf-8') as file:
                            for i in data:
                                file.writelines(f"{i}")
                        print('\n \n\u001b[3m' + 'Password Deleted' + '\u001b[0m \n \n')
                        if not data:
                            return True
                        break

                except ValueError or EOFError:
                    break



if __name__ == "__main__":
    main()