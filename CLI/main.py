'''
Name: SAURABH
Roll no.: 2501010045
Library Inventory Assignment
'''

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Library.inventory import LibraryInventory


def show_options():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search by Title")
    print("5. View All Books")
    print("6. Exit")


def main():
    store = LibraryInventory()

    while True:
        show_options()
        user_input = input("Enter choice: ")

        try:
            if user_input == "1":
                name = input("Enter Title: ")
                writer = input("Enter Author: ")
                code = input("Enter ISBN: ")

                if name and writer and code:
                    store.add_book(name, writer, code)
                else:
                    print("Error: All fields are required.")

            elif user_input == "2":
                code = input("Enter ISBN to issue: ")
                found = store.search_by_isbn(code)

                if found:
                    if found.issue():
                        store.save_books()
                        print(f"Book '{found.title}' issued successfully.")
                    else:
                        print("Error: Book is already issued.")
                else:
                    print("Error: Book not found.")

            elif user_input == "3":
                code = input("Enter ISBN to return: ")
                found = store.search_by_isbn(code)

                if found:
                    found.return_book()
                    store.save_books()
                    print(f"Book '{found.title}' returned successfully.")
                else:
                    print("Error: Book not found.")

            elif user_input == "4":
                term = input("Enter title to search: ")
                matches = store.search_by_title(term)

                if matches:
                    for item in matches:
                        print(item)
                else:
                    print("No matching books found.")

            elif user_input == "5":
                store.display_all()

            elif user_input == "6":
                print("Exiting...")
                return

            else:
                print("Invalid choice. Please try again.")

        except Exception as err:
            print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    main()