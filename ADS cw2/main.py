from book_class import Book
from periodical_class import Periodical
from audiobook_class import Audiobook
from borrower_class import Borrower
from administrator_class import Administrator
from librarytree_class import LibraryTree
from borrowerlist_class import BorrowerList
from borroweditems_class import BorrowedItemsLinkedList
import datetime
import csv

def main():
    library = LibraryTree()
    borrowers_file_path = input("Enter the full path to the CSV file containing borrower data: ")
    borrowers_file_path = borrowers_file_path.strip('"')
    borrower_list = create_borrower_database_from_csv(borrowers_file_path)
    borrowed_items_list = BorrowedItemsLinkedList()

    library.insert(Book("The Adventures of Sally", "Fiction", "English", ["Samantha Ruth", "Shannon Lee"], 2019))
    library.insert(Book("Classroom Chronicles: A Journey Through Education", "Non-fiction", "Malay",
                        ["Ciara Case", "Helena Brown"], 2001, "7094182233"))
    library.insert(Periodical("People", "Lifestyle", "English", ["Eliza David", "Miya Erickson"], 2023))
    library.insert(Audiobook("Escape Room", "Fiction", "English", ["Sue Rose"], 2023, "Hillary Tan", 360))

    admin = Administrator("ad101", "ad101ps", "Admin", "User")

    while True:
        print("\nLibrary System Menu:")
        print("1. Borrower Menu")
        print("2. Administrator Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            borrower_menu(borrower_list, library, borrowed_items_list)
        elif choice == "2":
            admin_menu(admin, borrower_list, library)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def create_borrower_database_from_csv(file_path):
    borrower_list = BorrowerList()

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Row from CSV:", row)
            borrower = Borrower(row["first_name"], row["last_name"], row["account_number"])
            borrower.set_username(row["username"])
            borrower.set_password(row["password"])
            borrower_list.add_borrower(borrower)

    return borrower_list

def borrower_menu(borrower_list, library, borrowed_items_list):
    while True:
        print("\nBorrower Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_borrower(borrower_list)
        elif choice == "2":
            borrower_login(borrower_list, library, borrowed_items_list)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(admin, borrower_list, library):
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if admin.authenticate(username, password):
        while True:
            print("\nAdministrator Menu:")
            print("1. Add Item to Library")
            print("2. Remove Item from Library")
            print("3. Display Library Catalog")
            print("4. View Borrowers List")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                add_item_to_library(library)
            elif choice == "2":
                remove_item_from_library(library)
            elif choice == "3":
                library.display_in_order()
            elif choice == "4":
                borrower_list.display_all_borrowers()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed.")

def register_borrower(borrower_list):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    account_number = input("Enter account number: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    borrower = Borrower(first_name, last_name, account_number)
    borrower.set_username(username)
    borrower.set_password(password)
    borrower_list.add_borrower(borrower)
    print("Borrower registered successfully.")

def borrower_login(borrower_list, library, borrowed_items_list):
    account_number = input("Enter account number: ")
    borrower = borrower_list.find_borrower_by_account_number(account_number)

    if borrower:
        while True:
            print("\nBorrower Actions Menu:")
            print("1. Rent Item")
            print("2. Return Item")
            print("3. View Rented Items")
            print("4. Pay Fine")
            print("5. Back to Borrower Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                rent_item(borrower, library, borrowed_items_list)
            elif choice == "2":
                return_item(borrower, library, borrowed_items_list)
            elif choice == "3":
                borrower.display_rented_items()
            elif choice == "4":
                pay_fine(borrower)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Borrower not found.")

def rent_item(borrower, library, borrowed_items_list):
    title = input("Enter the title of the item to rent: ")
    item = library.search(title)

    if item:
        if borrower.rent_item(item):
            borrowed_items_list.add_borrowed_item(borrower.account_number, item.title, str(datetime.date.today()))
            print("Item rented successfully.")
        else:
            print("Unable to rent item.")
    else:
        print("Item not found in library.")

def return_item(borrower, library, borrowed_items_list):
    title = input("Enter the title of the item to return: ")
    item = library.search(title)

    if item:
        if borrower.return_item(item):
            print("Item returned successfully.")
        else:
            print("Unable to return item.")
    else:
        print("Item not found in library.")

def pay_fine(borrower):
    amount = float(input("Enter the amount to pay: "))

    if borrower.pay_fine(amount):
        print("Fine paid successfully.")
    else:
        print("Partial payment made. Remaining fine amount:", borrower.fine_amount)

def add_item_to_library(library):
    item_type = input("Enter the type of item (Book/Periodical/Audiobook): ").strip().lower()
    title = input("Enter title: ")
    category = input("Enter category: ")
    language = input("Enter language: ")
    authors = input("Enter authors (comma separated): ").split(", ")
    year_published = int(input("Enter year published: "))

    if item_type == "book":
        isbn = input("Enter ISBN (optional): ")
        item = Book(title, category, language, authors, year_published, isbn)
    elif item_type == "periodical":
        item = Periodical(title, category, language, authors, year_published)
    elif item_type == "audiobook":
        narrator = input("Enter narrator: ")
        duration = int(input("Enter duration in minutes: "))
        item = Audiobook(title, category, language, authors, year_published, narrator, duration)
    else:
        print("Invalid item type.")
        return

    library.insert(item)
    print("Item added to library.")

def remove_item_from_library(library):
    title = input("Enter the title of the item to remove: ")
    removed_item = library.remove(title)
    if removed_item:
        print("Item '{}' removed from the library.".format(title))
    else:
        print("Item '{}' deleted".format(title))

if __name__ == "__main__":
    main()
