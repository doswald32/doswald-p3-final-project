# lib/cli.py
#!/user/bin/env python3

from helpers import (
    exit_program,
    list_patrons,
    patron_details
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
        elif choice == "2":
            add_customer()
        else:
            print("Invalid choice")


def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View customer database")
    print("2. View books")


def patron_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Select a patron to see additional details")
    print("2. Update a patron")
    print("3. Add a patron")
    print("4. Delete a patron")
    choice = input("> ")
    if choice == "1":
        patron_details()

if __name__ == "__main__":
    main()
