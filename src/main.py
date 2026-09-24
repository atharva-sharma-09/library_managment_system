from books import books, add_book, view_books, search_book
from students import students, add_student, view_students
from transactions import issued_books, issue_book, return_book, view_issued_books
from validation import valid_menu_choice
from reports import library_report
from storage import save_data, load_data


# Load previously saved data
loaded_books, loaded_students, loaded_issued_books = load_data()

books.extend(loaded_books)
students.extend(loaded_students)
issued_books.extend(loaded_issued_books)


while True:

    print("==LIBRARY MANAGEMENT SYSTEM==")
  

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Add Student")
    print("7. View Students")
    print("8. View Issued Books")
    print("9. Library Report")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if not valid_menu_choice(choice):

        continue

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book(books, students)

    elif choice == "5":
        return_book()

    elif choice == "6":
        add_student()

    elif choice == "7":
        view_students()

    elif choice == "8":
        view_issued_books()

    elif choice == "9":
        library_report(books, students, issued_books)

    elif choice == "10":
        save_data(books, students, issued_books)
        print("Data saved successfully.")
        print("Program closed.")
        break