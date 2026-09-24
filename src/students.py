students = []


def add_student():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")

    students.append([student_id, student_name])

    print("Student added successfully!")


def view_students():
    print("\n===== STUDENTS =====")

    if len(students) == 0:
        print("No students available.")
        return

    for student in students:
        print("ID:", student[0])
        print("Name:", student[1])
        print("----------------")


def find_student(student_id):
    for student in students:
        if student[0] == student_id:
            return student

    return None