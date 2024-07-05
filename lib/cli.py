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
    p_choice = input("> ")
    if p_choice.isdigit() and int(p_choice) <= Patron.table_length():
        list_books(int(p_choice), books_menu, patron_menu)
        books_menu(p_choice)
        return
    elif p_choice == "B" or p_choice == "b":
        main()
    elif p_choice == "A" or p_choice == "a":
        add_new_patron()
        list_patrons()
        patron_menu()
    elif p_choice == "E" or p_choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
        list_patrons()
        patron_menu()

    
def books_menu(p_choice):
    print("Please select the number of the book to its details")
    print("        or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new book for this patron")
    print("Press D or d to delete this patron")
    print("Press E or e to exit")
    b_choice = input("> ")
    if b_choice.isdigit() and int(b_choice) <= Patron.table_length():
        list_books(books_menu, patron_menu, p_choice)
    elif b_choice == "B" or b_choice == "b":
        list_patrons()
        patron_menu()
    elif b_choice == "A" or b_choice == "a":
        add_new_patron()
        books_menu()
    elif b_choice == "D" or b_choice == "d":
        update_patron()
        patron_menu()
    elif b_choice == "E" or b_choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
        books_menu()
         

if __name__ == "__main__":
    main()
