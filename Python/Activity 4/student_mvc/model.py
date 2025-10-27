# The Model represents the program’s data and logic.
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def update_grade(self, new_grade):
        """Update the student's grade."""
        self.grade = new_grade

    def __str__(self):
        """Return a string representation of the student."""
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"
