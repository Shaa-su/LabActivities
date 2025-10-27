# dito makikita ang display or ui ng activity 
def show_menu():
    print("\n+++++ Student Management System +++++")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Grade")
    print("4. Delete Student")
    print("5. Exit")

def get_student_details():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")
    return student_id, name, grade

def get_student_id():
    return input("Enter Student ID: ")

def get_new_grade():
    return input("Enter new grade: ")

def show_students(students):
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for student in students:
            print(student)

def show_message(message):
    print(message)
