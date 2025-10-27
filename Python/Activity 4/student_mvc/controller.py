from student_mvc.model import Student
import student_mvc.view as view

class StudentController:
    def __init__(self):
        self.students = []  

    def add_student(self):
        student_id, name, grade = view.get_student_details()
        # pang chekc if may duplicate
        for s in self.students:
            if s.student_id == student_id:
                view.show_message("Student ID already exists!")
                return
        new_student = Student(student_id, name, grade)
        self.students.append(new_student)
        view.show_message("Student added successfully!")

    def view_all_students(self):
        view.show_students(self.students)

    def update_student_grade(self):
        student_id = view.get_student_id()
        for s in self.students:
            if s.student_id == student_id:
                new_grade = view.get_new_grade()
                s.update_grade(new_grade)
                view.show_message("Grade updated successfully!")
                return
        view.show_message("Student not found!")

    def delete_student(self):
        student_id = view.get_student_id()
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                view.show_message("Student deleted successfully!")
                return
        view.show_message("Student not found!")
