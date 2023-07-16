import random
import string

#main function
def main():

    select_menu()

#Print the Main Menu
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

#Get password name from user
def get_name(data):
    while True:
        try:
            name = input("What is your password name?: ").strip()
            if not name:
                print("Password name can not be empty.")
                continue
            passwords = []
            with open("passwords.txt") as file:
                for line in file:
                    passwords.append(line.rstrip().split(" -")[0])
            if name in passwords:
                same_name(name, data)
            else:
                save_p(name)
            break
        except EOFError:
            return

#Save password to file
def save_p(name):
    while True:
        try:
            password = input("What is your password? (If you want to generate a new one, type 'g'): ").strip()
            if not password:
                print("Password can not be empty.")
                continue
            break
        except EOFError:
            return

    if password == "g":
        password = give_generated()
        print("Generated Password:", password)

    with open("passwords.txt", "a") as file:
        file.write(f"{name} - {password}\n")

    print('\n \n\u001b[3m' + 'New Password Saved' + '\u001b[0m')

#If the user wants to save a different password with the same name, save this password to file
def same1(name):
    while True:
        try:
            password = input("\nWhat is your password? (If you want to generate a new one, type 'g'): ").strip()
            if not password:
                print("\nPassword can not be empty.")
            else:
                if password == "g":
                    password = give_generated()
                    print("Generated Password:", password)

                with open("passwords.txt", "a") as file:
                    file.write(f"{name} - {password}\n")
                print('\n \n\u001b[3m' + 'New Password Saved' + '\u001b[0m')
                break

        except EOFError:
            return

#If the user wants to overwrite with a newpassword, update this password in the file
def same2(name, data):
    while True:
        try:
            password = input("\nWhat is your password? (If you want to generate a new one, type 'g'): ").strip()
            if not password:
                print("\nPassword can not be empty.")
            else:
                if password == "g":
                    password = give_generated()
                for line in data:
                    if name in line:
                        line_num = data.index(line) + 1

                name = (data[line_num - 1].split(" -"))[0]
                data[line_num - 1] = f"{name} - {password}\n"
                with open('passwords.txt', 'w', encoding='utf-8') as file:
                    for i in data:
                        file.write(f"{i}")

                print('\n \n\u001b[3m' + 'Password Edited' + '\u001b[0m')
                break
        except EOFError:
            return

#If there is a password with the same name, ask the user what they want to do
def same_name(name, data):
    print("\n\nA password with this name already exists among the saved passwords.")
    print("What do you want to do?")
    print("[1] Save a new password with the same name")
    print("[2] Overwrite with a new password")
    print("[3] Back to Menu")
    while True:
        try:
            option = input("Select the option you want to do: ").strip()

            if not option or not (0 < int(option) and 4 > int(option)):
                print("Invalid Option")
            elif int(option) == 1:
                same1(name)
                break
            elif int(option) == 2:
                same2(name, data)
                break
            elif int(option) == 3:
                break

        except EOFError:
            break
        except ValueError:
            print("Invalid Option")

#Check what the user has selected in the main menu
def select_menu():
    while True:
        try:
            data  = []
            with open('passwords.txt', 'r', encoding='utf-8') as file:
                for  line in file:
                    data.append(f"{line.rstrip()} \n")
            menu()
            option = int(input("Select the option you want to do (You can always go back by pressing CTRL+D): "))

            if option == 1:
                if data:
                    select_menu2(data)
                else:
                    print("\n")
                    print("There are no saved passwords. ")
            elif option == 2:
                get_name(data)
            elif option == 3:
                password=give_generated()
                if password != None:
                    print(f"\n\nGenerated Password: {password}")
            elif option == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid option ")
        except EOFError:
            break

#Check what the user has selected in the saved passwords menu
def select_menu2(data):
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
                while True:
                    try:
                        a = delete_menu(data)
                        if a == True:
                            return True
                    except EOFError:
                        break
                    break
            elif option2 == 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid option ")
        except EOFError:
            break

#Generate and return password
def give_generated():
    try:
        while True:
            spec_c = input("Do you want a special character in the password? [Y(y)/N(n)]: ")
            if spec_c.strip() == "Y" or spec_c.strip() == "y" or spec_c.strip() == "N" or spec_c.strip() == "n":
                break
            else:
                print("Invalid Option")
        while True:
            if spec_c.strip() == "Y" or spec_c.strip() == "y":
                try:
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
                except ValueError:
                    print("Password length must be between 5 and 128. ")

            elif spec_c.strip() == "N" or spec_c.strip() == "n":
                try:
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
                except ValueError:
                    print("Invalid Option")
            else:
                print("Invalid Option")
                continue
    except EOFError:
        return None

#Return passwords in the file
def get_passwords():
    passwords = []
    with open("passwords.txt") as file:
        for i, line in enumerate(file, start=1):
            passwords.append(f"{i} {line.rstrip()} ")
    return passwords

#Edit the password as requested by the user.
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
            line = input("Enter the line number of the password you want to edit: ").strip()
            if not line.isdigit():
                print("Invalid line")
                continue
            line_num = int(line)
            if line_num < 1 or line_num > len(data):
                print("Invalid line")
                continue
            password = input("What is your new password? (If you want to generate a new one, type 'g'): ").strip()
            if password == "g":
                password = give_generated().strip()
            name = data[line_num - 1].split(" -")[0]
            data[line_num - 1] = f"{name} - {password}\n"
            with open('passwords.txt', 'w', encoding='utf-8') as file:
                for i in data:
                    file.write(f"{i}")
                print('\n \n\u001b[3m' + 'Password Edited' + '\u001b[0m')
            break
        except ValueError:
            print("Invalid line")
            continue
        except EOFError:
            break

#Delete password or passwords
def delete_menu(data):
    print("\n")
    print("================")
    print("Delete Password")
    print("================")
    for password in get_passwords():
        print(password)
    print("================")
    while data:
        try:
            line = int(input("Enter the number of the line you want to delete (If you want to delete all, type '0'): ").strip())

            if line < 0 or line > len(data):
                print("Invalid line")

            elif line == 0:
                data.clear()
                with open('passwords.txt', 'w', encoding='utf-8') as file:
                    for i in data:
                        file.writelines(f"{i}")
                print('\n \n\u001b[3m' + 'All Saved Passwords Deleted' + '\u001b[0m')
                return True
            else:
                del data[line-1]
                with open('passwords.txt', 'w', encoding='utf-8') as file:
                    for i in data:
                        file.writelines(f"{i}")
                print('\n \n\u001b[3m' + 'Password Deleted' + '\u001b[0m \n \n')
                if not data:
                    return True
        except ValueError:
            print("Invalid line")
        except EOFError:
            break


if __name__ == "__main__":
    main()