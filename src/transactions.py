issued_books = []


def issue_book(books, students):
    student_id = input("Enter student ID: ")
    book_id = input("Enter book ID: ")

    student_found = False
    book_found = False

    for student in students:
        if student[0] == student_id:
            student_found = True

    for book in books:
        if book[0] == book_id:
            book_found = True

    if not student_found:
        print("Student not found.")
        return

    if not book_found:
        print("Book not found.")
        return

    for issued in issued_books:
        if issued[1] == book_id:
            print("Book is already issued.")
            return

    issued_books.append([student_id, book_id])

    print("Book issued successfully!")


def return_book():
    student_id = input("Enter student ID: ")
    book_id = input("Enter book ID: ")

    for issued in issued_books:
        if issued[0] == student_id and issued[1] == book_id:
            issued_books.remove(issued)
            print("Book returned successfully!")
            return

    print("No such issue record found.")


def view_issued_books():
    print("\n===== ISSUED BOOKS =====")

    if len(issued_books) == 0:
        print("No books are currently issued.")
        return

    for issued in issued_books:
        print("Student ID:", issued[0])
        print("Book ID:", issued[1])
        print("----------------")