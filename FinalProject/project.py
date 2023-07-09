def main():
    select_menu()

def get_passwords():
    with open("passwords.txt") as file:

        for i, line in enumerate(file, start=1):
            print(f"{i} {line.rstrip()}")




def new_password():

    name = input("What is your password name?: ")
    password = input("What is your password?: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{name} - {password}\n")


def get_account_name():
    account = str(input("What is your account name?: "))
    return account
def menu():
    print("================")
    print("Password Manager")
    print("================")
    print("[1] List saved passwords")
    print("[2] Save new password")
    print("[3] Generate new password")
    print("[4] Quit Program")
    print("================")

def select_menu():
    while True:
        try:
            menu()
            option = int(input("Select the option you want to do: "))
            if option == 1:
                select_menu2()
            elif option == 2:
                new_password()
            elif option == 3:
                print(3)
            elif option == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid option ")
        except EOFError:
            break

def select_menu2():
    while True:
        try:
            print("\n")
            print("================")
            print("Saved Passwords")
            print("================")
            get_passwords()
            print("================")
            print("[1] Edit Passwords")
            print("[2] Delete Passwords")
            print("[3] Back to Menu")
            option2 = int(input("Select the option you want to do: "))

            if option2 == 1:
                print(1)
            elif option2 == 2:
                print(2)
            elif option2 == 3:
                print(3)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid option ")

#def edit_p():



if __name__ == "__main__":
    main()