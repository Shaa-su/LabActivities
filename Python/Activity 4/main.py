# Dito ni import ang controller at view modules 

from student_mvc.controller import StudentController
import student_mvc.view as view

def main():
    
    controller = StudentController()

    # dito gumamit ng loop hindi ito tititgil hangang hindi nag equal to 5 which is exit 
    while True:
        view.show_menu()
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
            view.show_mesage("Exiting program. Byee byeee")
            break
        else:
            # pang sapo
            view.show_mesage("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
