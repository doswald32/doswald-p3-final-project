# lib/cli.py
#!/user/bin/env python3

from helpers import (
    exit_program,
    list_patrons
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_patrons()
        elif choice == "2":
            add_customer()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Access customer database")
    print("2. Add new customer")


if __name__ == "__main__":
    main()
