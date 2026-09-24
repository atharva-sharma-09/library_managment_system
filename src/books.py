books = []


def add_book():
    book_id = input("Enter book ID: ")
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")

    books.append([book_id, book_name, author])

    print("Book added successfully!")


def view_books():
    print("\n===== BOOKS =====")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        print("ID:", book[0])
        print("Name:", book[1])
        print("Author:", book[2])
        print("----------------")


def search_book():
    search_id = input("Enter book ID to search: ")

    for book in books:
        if book[0] == search_id:
            print("\nBook found!")
            print("ID:", book[0])
            print("Name:", book[1])
            print("Author:", book[2])
            return

    print("Book not found ")