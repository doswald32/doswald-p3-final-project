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
    main_menu()
    choice = input("> ")
    if choice == "L" or choice == "l":
        list_patrons()
        patron_menu()
    elif choice == "E" or choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
        main()
            


def main_menu():
    print("Please select an option:")
    print("Press L or l to see a list of patrons")
    print("Press E or e to exit")


def patron_menu():
    print("Please select patron number to see their books")
    print("         or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new patron")
    print("Press E or e to exit")
    choice = input("> ")
    if choice.isdigit() and int(choice) <= Patron.table_length():
        list_books(int(choice), books_menu, patron_menu)
        books_menu()
    elif choice == "B" or choice == "b":
        main()
    elif choice == "A" or choice == "a":
        add_new_patron()
        list_patrons()
        patron_menu()
    elif choice == "E" or choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
        list_patrons()
        patron_menu()

    
def books_menu():
    print("Please select the number of the book to its details")
    print("        or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new book for this patron")
    print("Press D or d to delete this patron")
    print("Press E or e to exit")
    choice = input("> ")
    if choice.isdigit() and int(choice) <= Patron.table_length():
        list_books(choice)
    elif choice == "B" or choice == "b":
        list_patrons()
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
        books_menu()
         

if __name__ == "__main__":
    main()
