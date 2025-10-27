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
