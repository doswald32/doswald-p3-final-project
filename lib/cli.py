# lib/cli.py
#!/user/bin/env python3

from models.patron import Patron

from helpers import (
    exit_program,
    list_patrons,
    update_patron,
    list_books
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
    print("Please select the number of the patron to see their books")
    print("         or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new patron")
    print("Press E or e to exit")
    choice = input("> ")
    if choice == "1" or choice == "2":
         list_books(choice)
    elif choice == "B" or choice == "b":
         main()
    elif choice == "B":
        list_patrons()
        patron_menu()
    elif choice == "2":
        update_patron()
        patron_menu()
         

if __name__ == "__main__":
    main()
