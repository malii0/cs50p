# Password Manager
Manage Your Passwords with Ease!

![Downloads](https://img.shields.io/github/downloads/malii0/cs50p/total) ![Contributors](https://img.shields.io/github/contributors/malii0/cs50p?color=dark-green) ![Issues](https://img.shields.io/github/issues/malii0/cs50p) ![License](https://img.shields.io/github/license/malii0/cs50p) 
## Before you Start
You can access the short video where I explain my project through this link: [Project Link](https://youtu.be/gFjPwhb2cC4)


## Table of contents

- [Password Manager](#password-manager)
  - [About The Project](#about-the-project)
  - [Features](#features)
  - [Built With](#built-with)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Note](#note)
  - [License](#license)

## About The Project

The Password Manager is a Python-based application that allows users to securely manage their passwords and sensitive information. It provides a user-friendly interface for saving, generating, editing, and deleting passwords. With this Password Manager, users can easily organize and protect their login credentials and other confidential data.


## Features

- Save Passwords: Users can save their passwords by providing a name for the password and entering the actual password. They also have the option to generate a secure password automatically.

- Generate Passwords: The Password Manager can generate strong and secure passwords with customizable options. Users can specify the length of the password and choose whether to include special characters.

- Edit Passwords: Users can edit their existing passwords. They can select a password from the list and update it with a new password or generate a new one.

- Delete Passwords: The Password Manager allows users to delete individual passwords or all saved passwords at once. This helps users keep their password list up to date and remove any unnecessary entries.

- List Passwords: Users can view a list of all saved passwords, including the name and corresponding password for each entry. This provides an overview of their password collection.

## Built With

- Python: The programming language used to develop the project.
- Random: Python module for generating random passwords.
- String: Python module for working with strings.
- Subprocess: Python module for running shell commands.
- File I/O: Python for reading and writing data to files.


## Usage
<details>
<summary>1. Test before start </summary>

  - If not installed, install pytest before testing
       ```bash
         pip install pytest
       ```
  - After the installation, you can test
       ```bash
         pytest test_project.py
       ```
</details>

<details>
<summary>2. Run the project.py file:</summary>

   ```bash
     python project.py
   ```
</details>

<details>
<summary>3. The Password Manager menu will be displayed.</summary>

</details>

<details>
<summary>4. Follow the on-screen instructions to manage your passwords:</summary>

 - List saved passwords, save new passwords, generate new passwords, edit passwords, and delete passwords.
   - You can see the main menu when you start the program.
   
       ```bash
         ================
         Password Manager
         ================
         [1] List saved passwords
         [2] Save new password
         [3] Generate new password
         [4] Quit Program
         ================
         Select the option you want to do (You can always go back by pressing CTRL+D): 
       ```
    - You can save your new passwords on the "Save new password" menu.
   
       ```bash
       ================
       Password Manager
       ================
       [1] List saved passwords
       [2] Save new password
       [3] Generate new password
       [4] Quit Program
       ================
       Select the option you want to do (You can always go back by pressing CTRL+D):
       What is your password name?: your_password_name
       What is your password? (If you want to generate a new one, type 'g'): your_password
        ```
   - Now you can see your saved passwords on the "Saved Passwords" menu.
       ```bash
       ================
       Saved Passwords
       ================
       1 your_password_name - your_password
       ================
       [1] Edit password
       [2] Delete Password
       [3] Back to Menu
       ================
       Select the option you want to do:
        ```
    - You can edit your passwords on the "Saved Passwords" menu. (Option 1)
   
       ```bash
       ================
       Saved Passwords
       ================
       1 your_password_name - your_password
       ================
       Enter the line number you want to edit: 1
       What is your new password (If you want to generate new one, type 'g'): your_edited_password

       Password Edited
        ```
   - You can delete your password or passwords on the "Saved Passwords" menu. (Option 2)
       ```bash
       ================
       Saved Passwords
       ================
       1 your_password_name - your_edited_password
       ================
       Enter the line number you want to delete (If you want to delete all type '0'): 1
       

       Password Deleted
        ```
    - You can generate new passwords on the "Generate new password" menu or whenever you are asked to enter a password.
       ```bash
       ================
       Password Manager
       ================
       [1] List saved passwords
       [2] Save new password
       [3] Generate new password
       [4] Quit Program
       ================
       Select the option you want to do (You can always go back by pressing CTRL+D):
       Do you want a special character in the password [Y(y)/N(n)]: y
       Enter the password length: 13


       Generated Password: ci%z0h_@ib2YW
        ```
</details>

## Contributing

Thank you for considering contributing to the Password Manager project! I welcome any contributions that can help improve the project and make it even better. To ensure a smooth and collaborative development process, please follow these guidelines:

### Creating A Pull Request

1. Fork the repository on GitHub.
2. Create a new branch for your contribution:
   - Use a descriptive and meaningful branch name.
   - Branch off from the main branch (master or main).
3. Make your changes:
   - Write clean and well-documented code.
   - Ensure your changes align with the project's coding style.
   - Test your changes thoroughly.
4. Commit your changes:
   - Provide clear and concise commit messages.
   - Reference any relevant issues or pull requests.
   - Push your changes to your forked repository.
6.Submit a pull request:
   - Clearly describe the purpose of your pull request.
   - Provide any necessary additional context or information.
   - Be open to feedback and discussion regarding your contribution.

I will review your pull request as soon as possible and provide any necessary feedback or suggestions. Thank you for your contribution!

## Note

It is important to emphasize that the Password Manager is intended for personal use and should be used responsibly. Users are advised to take necessary precautions to protect their passwords and ensure the security of their devices. The Password Manager does not guarantee absolute security and is not liable for any loss or damage resulting from the use of the application.

  
## License

Distributed under the MIT License. See [LICENSE](https://github.com/malii0/cs50p/blob/main/LICENSE) for more information.
