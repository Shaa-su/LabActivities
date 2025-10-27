
#+++++MODEL+++++
#dito galing yung mga data pang store and then mag mga logic dinnn
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"

#+++++VIEW+++++
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

#+++++CONTROLLER+++++
class StudentController:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id, name, grade = get_student_details()
        # pang chekc if may duplicate
        for s in self.students:
            if s.student_id == student_id:
                show_message("Student ID already exists!")
                return
        new_student = Student(student_id, name, grade)
        self.students.append(new_student)
        show_message("Student added successfully!")

    def view_all_students(self):
        show_students(self.students)

    def update_student_grade(self):
        student_id = get_student_id()
        for s in self.students:
            if s.student_id == student_id:
                new_grade = get_new_grade()
                s.update_grade(new_grade)
                show_message("Grade updated successfully!")
                return
        show_message("Student not found!")

    def delete_student(self):
        student_id = get_student_id()
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                show_message("Student deleted successfully!")
                return
        show_message("Student not found!")

#+++++MAIN+++++
def main():
    controller = StudentController()

    # dito gumamit ng loop hindi ito tititgil hangang hindi nag equal to 5 which is exit
    while True:
        show_menu()
        choice = input("Enter choise: ")

        if choice == "1":
            # kapag 1 mag add stduent
            controller.add_student()
        elif choice == "2":
            # Kapag 2 view lang
            controller.view_all_students()
        elif choice == "3":
            # kung 3 update need muna Id then perefered score nasa controller.py yung function
            controller.update_student_grade()
        elif choice == "4":
            # almost same sa 3 need din ng id pero delete naman ito
            controller.delete_student()
        elif choice == "5":
            # 5 naman ay pang exit lang kagaya ng sabi ko nung una
            show_message("Exiting program. Byee byeee")
            break
        else:
            # pang sapo
            show_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()