
from student_mvc.controller import StudentController
import student_mvc.view as view

def main():
    controller = StudentController()

    while True:
        view.show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            controller.add_student()
        elif choice == "2":
            controller.view_all_students()
        elif choice == "3":
            controller.update_student_grade()
        elif choice == "4":
            controller.delete_student()
        elif choice == "5":
            view.show_message("Exiting program. Goodbye!")
            break
        else:
            view.show_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
