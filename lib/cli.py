# lib/cli.py
#!/user/bin/env python3

from models.patron import Patron

from helpers import (
    exit_program,
    list_patrons,
    update_patron,
    list_books,
    add_new_patron
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
    if int(choice) <= Patron.table_length():
         list_books(choice)
         books_menu()
    elif choice == "B" or choice == "b":
         main()
    elif choice == "A" or choice == "a":
        list_patrons()
        patron_menu()
    elif choice == "E" or choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
    


def books_menu():
    print("Please select the number of the book to its details")
    print("        or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new book for this patron")
    print("Press D or d to delete this patron")
    print("Press E or e to exit")
    choice = input("> ")
    if choice == "1" or "2":
        list_books(choice)
        books_menu()
    elif choice == "B" or choice == "b":
        patron_menu()
    elif choice == "A" or choice == "a":
        add_new_patron()
        books_menu()
    elif choice == "D" or choice == "d":
        update_patron()
        patron_menu()
    elif choice == "E" or choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
         

if __name__ == "__main__":
    main()
