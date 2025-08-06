class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, book_name):
        # Add a book to the library
        self.books.append(book_name)
        print(f'Book "{book_name}" added successfully.')

    def remove_book(self, book_name):
        # Remove a book from the library if it exists
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'Book "{book_name}" removed successfully.')
        else:
            print(f'Book "{book_name}" not found in the library.')

    def search_book(self, book_name):
        # Search for a book in the library
        if book_name in self.books:
            print(f'Book "{book_name}" is available in the library.')
        else:
            print(f'Book "{book_name}" is not available in the library.')

    def display_books(self):
        # Display all books in the library
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(f'- {book}')
        else:
            print("No books available in the library.")


class Members:
    def __init__(self):
        # Initialize an empty list to store members
        self.members = []

    def register_member(self, member_name):
        # Register a new member
        self.members.append(member_name)
        print(f'Member "{member_name}" registered successfully.')

    def remove_member(self, member_name):
        # Remove a member if they exist
        if member_name in self.members:
            self.members.remove(member_name)
            print(f'Member "{member_name}" removed successfully.')
        else:
            print(f'Member "{member_name}" not found.')

    def display_members(self):
        # Display all registered members
        if self.members:
            print("Registered Members:")
            for member in self.members:
                print(f'- {member}')
        else:
            print("No members registered.")


class Transactions:
    def __init__(self):
        # Initialize lists to store borrowed books and transaction history
        self.borrowed_books = []
        self.transaction_history = []

    def borrow_book(self, member_name, book_name):
        # Record a book borrowing transaction
        self.borrowed_books.append((member_name, book_name))
        self.transaction_history.append(
            f'Member "{member_name}" borrowed book "{book_name}".')
        print(f'Member "{member_name}" borrowed book "{book_name}".')

    def return_book(self, member_name, book_name):
        # Record a book returning transaction
        if (member_name, book_name) in self.borrowed_books:
            self.borrowed_books.remove((member_name, book_name))
            self.transaction_history.append(
                f'Member "{member_name}" returned book "{book_name}".')
            print(f'Member "{member_name}" returned book "{book_name}".')
        else:
            print(
                f'No record found for member "{member_name}" borrowing book "{book_name}".')

    def display_transactions(self):
        # Display currently borrowed books
        if self.borrowed_books:
            print("Borrowed Books:")
            for member, book in self.borrowed_books:
                print(f'Member: {member}, Book: {book}')
        else:
            print("No transactions recorded.")

    def display_transaction_history(self):
        # Display the history of all borrowing and returning transactions
        if self.transaction_history:
            print("Transaction History:")
            for record in self.transaction_history:
                print(record)
        else:
            print("No transaction history recorded.")


def main():
    # Create objects for library, members, and transactions
    library = Library()
    members = Members()
    transactions = Transactions()

    while True:
        # Display main menu
        print("\nLibrary Management System")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Transaction Track")
        print("4. Exit")

        # Get user choice for main menu
        main_choice = input("Enter your choice (1-4): ")

        if main_choice == '1':
            # Book Management Menu
            print("\nBook Management")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Search Book")
            print("4. Display Books")
            book_choice = input("Enter your choice (1-4): ")

            if book_choice == '1':
                book_name = input("Enter book name to add: ")
                library.add_book(book_name)
            elif book_choice == '2':
                book_name = input("Enter book name to remove: ")
                library.remove_book(book_name)
            elif book_choice == '3':
                book_name = input("Enter book name to search: ")
                library.search_book(book_name)
            elif book_choice == '4':
                library.display_books()
            else:
                print("Invalid choice!")

        elif main_choice == '2':
            # Member Management Menu
            print("\nMember Management")
            print("1. Register Member")
            print("2. Remove Member")
            print("3. Display Members")
            member_choice = input("Enter your choice (1-3): ")

            if member_choice == '1':
                member_name = input("Enter member name to register: ")
                members.register_member(member_name)
            elif member_choice == '2':
                member_name = input("Enter member name to remove: ")
                members.remove_member(member_name)
            elif member_choice == '3':
                members.display_members()
            else:
                print("Invalid choice!")

        elif main_choice == '3':
            # Transaction Management Menu
            print("\nTransaction Track")
            print("1. Borrow Book")
            print("2. Return Book")
            print("3. Display Transactions")
            print("4. Display Transaction History")
            transaction_choice = input("Enter your choice (1-4): ")

            if transaction_choice == '1':
                member_name = input("Enter member name: ")
                book_name = input("Enter book name to borrow: ")
                transactions.borrow_book(member_name, book_name)
            elif transaction_choice == '2':
                member_name = input("Enter member name: ")
                book_name = input("Enter book name to return: ")
                transactions.return_book(member_name, book_name)
            elif transaction_choice == '3':
                transactions.display_transactions()
            elif transaction_choice == '4':
                transactions.display_transaction_history()
            else:
                print("Invalid choice!")

        elif main_choice == '4':
            print("Exiting...")
            break


if __name__ == '__main__':
    main()
