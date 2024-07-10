# lib/cli.py
#!/user/bin/env python3

from models.patron import Patron
from models.book import Book
from helpers import (
    exit_program,
    list_patrons,
    list_books,
    add_new_patron,
    add_new_book,
    delete_patron,
    delete_book,
    update_patron,
    update_book,
    print_book_details
)


def main():
    main_menu()
    choice = input("> ")
    if choice == "L" or choice == "l":
        print("")
        list_patrons()
        print("")
        patron_menu()
    elif choice == "E" or choice == "e":
        exit_program()
    else:
        print("")
        print("Please make a valid selection")
        main()
            

def main_menu():
    print("")
    print("WELCOME!")
    print("")
    print("Please select an option:")
    print("")
    print("Press L or l to see a list of patrons")
    print("Press E or e to exit")
    print("")


def patron_menu():
    print("")
    print("Please select a patron ID to see their books")
    print("         or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new patron")
    print("Press E or e to exit")
    p_choice = input("> ")
    if p_choice.isdigit() and int(p_choice) <= len(Patron.get_all()):
        patron = Patron.get_all()[int(p_choice) - 1]
        print("\n", patron.first_name, patron.last_name, "\n")
        list_books(patron)
        books_menu(patron)
    elif p_choice == "B" or p_choice == "b":
        main()
    elif p_choice == "A" or p_choice == "a":
        add_new_patron()
        print("")
        list_patrons()
        print("")
        patron_menu()
    elif p_choice == "E" or p_choice == "e":
        exit_program()
    else:
        print("")
        print("Please make a valid selection")
        print("")
        list_patrons()
        print("")
        patron_menu()


def books_menu(patron):
    print("")
    print("Please select the number of a book to see its details. If a patron has no books, select one of the options below.")
    print("")
    print("Press B or b to go back to the previous menu")
    print("Press U or u to update this patron")
    print("Press A or a to add a new book for this patron")
    print("Press D or d to delete this patron")
    print("Press E or e to exit")
    b_choice = input("> ")
    if b_choice.isdigit() and int(b_choice) <= len(patron.books()):
        book = patron.books()[int(b_choice) - 1]
        print_book_details(book)
        single_book_menu(patron, book)
    elif b_choice == "B" or b_choice == "b":
        print("")
        list_patrons()
        print("")
        patron_menu()
    elif b_choice == "U" or b_choice == "u":
        update_patron(patron)
        print("")
        print("Patron successfully updated!")
        print("")
        list_patrons()
        print("")
        patron_menu()
    elif b_choice == "A" or b_choice == "a":
        add_new_book(patron)
        print("\n", patron.first_name, patron.last_name, "\n")
        print("")
        list_books(patron)
        print("")
        books_menu(patron)
    elif b_choice == "D" or b_choice == "d":
        delete_patron(patron)
        print("")
        print("Patron successfully deleted.")
        print("")
        list_patrons()
        print("")
        patron_menu()
    elif b_choice == "E" or b_choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
        print("\n", patron.first_name, patron.last_name, "\n")
        list_books(patron)
        books_menu(patron)

def single_book_menu(patron, book):
    print("")
    print("Please select an option")
    print("")
    print("Press B or b to go back to the previous menu")
    print("Press D or d to delete this book")
    print("Press U or u to update book")
    print("Press E or e to exit")
    choice = input("> ")
    if choice == "B" or choice == "b":
        print("\n", patron.first_name, patron.last_name, "\n")
        list_books(patron)
        books_menu(patron)
    elif choice == "D" or choice == "d":
        delete_book(book)
        print("")
        print("Book successfully deleted.")
        print("")
        list_patrons()
        print("")
        patron_menu()
    elif choice == "U" or choice == "u":
        update_book(book, patron)
        print("")
        print("Book successfully updated!")
        print("")
        list_books(patron)
        if len(patron.books()) > 0:
            books_menu(patron)
        else:
            patron_menu()
    elif choice == "E" or choice == "e":
        exit_program()
    else:
        print("")
        print("Please make a valid selection")
        print("")
        list_books(patron)
        books_menu(patron)
         

if __name__ == "__main__":
    main()
