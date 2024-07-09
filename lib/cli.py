# lib/cli.py
#!/user/bin/env python3

from models.patron import Patron
from models.book import Book
from helpers import (
    exit_program,
    list_patrons,
    list_books,
    add_new_patron,
    display_book_info,
    print_choice_name,
    add_new_book,
    delete_patron,
    delete_book,
    update_book
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
    print("")
    print("WELCOME!")
    print("")
    print("Please select an option:")
    print("")
    print("Press L or l to see a list of patrons")
    print("Press E or e to exit")
    print("")


def patron_menu():
    print("Please select a patron ID to see their books")
    print("         or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new patron")
    print("Press E or e to exit")
    p_choice = input("> ")
    if p_choice.isdigit() and int(p_choice) <= Patron.table_length():
        patron = Patron.get_all()[int(p_choice) - 1]
        print(patron.first_name, patron.last_name)
        list_books(patron)
        # print_choice_name(p_choice)
        list_books(int(p_choice), books_menu, no_books_menu)
        # books_menu(p_choice)
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

    
def no_books_menu(p_choice):
    print("")
    print("Please make a selection")
    print("")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new book for this patron")
    print("Press D or d to delete this patron")
    print("Press E or e to exit")
    choice = input("> ")
    if choice == "B" or choice == "b":
        list_patrons()
        patron_menu()
    elif choice == "A" or choice == "a":
        title = input("Enter book's title: ")
        author = input("Enter book's author: ")
        pages = int(input("Enter number of pages: "))
        description = input("Enter brief description: ")
        add_new_book(title, author, pages, description, int(p_choice))
        print_choice_name(p_choice)
        list_books(p_choice, books_menu, patron_menu)
    elif choice == "D" or choice == "d":
        delete_patron(p_choice)
        patron_menu()
    elif choice == "E" or choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
        list_books(int(p_choice), books_menu, no_books_menu)


def books_menu(p_choice):
    print("")
    print("Please select the number of the book to see its details")
    print("        or")
    print("Press B or b to go back to the previous menu")
    print("Press A or a to add a new book for this patron")
    print("Press D or d to delete this patron")
    print("Press E or e to exit")
    b_choice = input("> ")
    if b_choice.isdigit() and int(b_choice) <= Book.table_length():
        display_book_info(p_choice, b_choice)
        single_book_menu(p_choice, b_choice)
    elif b_choice == "A" or b_choice == "a":
        title = input("Enter book's title: ")
        author = input("Enter book's author: ")
        pages = input("Enter number of pages: ")
        description = input("Enter brief description: ")
        add_new_book(title, author, pages, description, int(p_choice))
        print_choice_name(p_choice)
        list_books(p_choice, books_menu, patron_menu)
    elif b_choice == "B" or b_choice == "b":
        list_patrons()
        patron_menu()
    elif b_choice == "D" or b_choice == "d":
        delete_patron(p_choice)
        patron_menu()
    elif b_choice == "E" or b_choice == "e":
        exit_program()
    else:
        print("Please make a valid selection")
        print_choice_name(p_choice)
        list_books(int(p_choice), books_menu, patron_menu)

def single_book_menu(p_choice, b_choice):
    print("")
    print("Please select an option")
    print("")
    print("Press B or b to go back to the previous menu")
    print("Press D or d to delete this book")
    print("Press U or u to update book")
    print("Press E or e to exit")
    f_choice = input("> ")
    if f_choice == "B" or f_choice == "b":
        print_choice_name(p_choice)
        list_books(p_choice, books_menu, patron_menu)
        books_menu(p_choice)
    elif f_choice == "D" or f_choice == "d":
        delete_book(p_choice, b_choice).delete()
        list_patrons()
        patron_menu()
    elif f_choice == "U" or f_choice == "u":
        # I have patron and I have book passed in
        title = input("Enter book's title: ")
        if title == "":
            title = book.title
        author = input("Enter book's author: ")
        pages = input("Enter number of pages: ")
        description = input("Enter book description: ")
        breakpoint()
        book.update(title, author, pages, description, patron.id)
        list_books(p_choice, books_menu, patron_menu)
        if len(patron.books()) > 0:
            books_menu(patron)
        else:
            patron_menu()
    elif f_choice == "E" or f_choice == "e":
        exit_program()
    else:
        print("")
        print("Please make a valid selection")
        print("")
        list_books(int(p_choice), books_menu, patron_menu)
         

if __name__ == "__main__":
    main()
