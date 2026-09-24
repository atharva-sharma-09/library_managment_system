def save_data(books, students, issued_books):

    with open("library_data.txt", "w") as file:

        file.write("BOOKS\n")

        for book in books:
            file.write(book[0] + "," + book[1] + "," + book[2] + "\n")

        file.write("STUDENTS\n")

        for student in students:
            file.write(student[0] + "," + student[1] + "\n")

        file.write("ISSUED_BOOKS\n")

        for issued in issued_books:
            file.write(issued[0] + "," + issued[1] + "\n")


def load_data():

    books = []
    students = []
    issued_books = []

    try:
        with open("library_data.txt", "r") as file:

            section = ""

            for line in file:
                line = line.strip()

                if line == "BOOKS":
                    section = "books"

                elif line == "STUDENTS":
                    section = "students"

                elif line == "ISSUED_BOOKS":
                    section = "issued"

                elif line != "":

                    data = line.split(",")

                    if section == "books":
                        books.append(data)

                    elif section == "students":
                        students.append(data)

                    elif section == "issued":
                        issued_books.append(data)

    except FileNotFoundError:
        pass

    return books, students, issued_books