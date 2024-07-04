# lib/cli.py
#!/user/bin/env python3

from models.patron import Patron

from helpers import (
    exit_program,
    list_patrons,
    update_patron
)


def main():
    # while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_patrons()
            patron_menu()
        else:
            print("Invalid choice")


def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See patrons")


def patron_menu():
    print("Please select an option:")
    print("0. Go back to the previous menu")
    print("1. See patrons list")
    print("2. Update a patron")
    print("3. Add a patron")
    print("4. Delete a patron")
    print("5. Exit the program")
    choice = input("> ")
    if choice == "0":
         main()
    if choice == "1":
        list_patrons()
        patron_menu()
    elif choice == "2":
        update_patron()
        patron_menu()
         

if __name__ == "__main__":
    main()
