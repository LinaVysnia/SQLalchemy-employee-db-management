from UI.employeeUI import *
from UI.departmentUI import *
from UI.projectUI import *

def run_main_UI():
        
    while True:
        user_choice = input("""Enter a corresponding number to:
    1 - To view all employees
    2 - To add an employee
    3 - To update employees information
    4 - To delete an employee entry
    5 - To view all departments
    6 - To add a department
    7 - To update department's information
    8 - To view all employees in a department
    9 - To view all the projects
    10 - To add a project
    11 - To edit a project
    12 - To view employees working on a specific project
    13 - To view selected employee's projects
    14 - To edit employees working on a project
    Q - To quit\n
    Your choice: """)
        
        if user_choice.strip().lower() == "q":
            print("Quitting...")
            break

        else:
            try:
                user_choice = int(user_choice)
                if user_choice not in list(range(1,15)): #update this when adding more UI options
                    raise Exception
            except Exception as ex:
                print(f"{user_choice} isn't a valid choice, please make a selection again.\n")

                continue
            
            if user_choice == 1:
                view_employees()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 2:
                run_add_employee_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 3:
                run_update_employee_UI()
                input("Press enter to return to the main menu")
                print()
            
            elif user_choice == 4:
                run_delete_employee_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 5:
                view_departments()
                input("Press enter to return to the main menu")
                print()
            
            elif user_choice == 6:
                run_add_department_UI()
                input("Press enter to return to the main menu")
                print()
            
            elif user_choice == 7:
                run_update_department_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 8:
                run_view_departments_employees_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 9:
                view_projects()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 10:
                add_project_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 11:
                edit_project_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 12:
                view_projects_employees_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 13:
                view_employees_projects_UI()
                input("Press enter to return to the main menu")
                print()

            elif user_choice == 14:
                edit_projects_employees_UI()
                input("Press enter to return to the main menu")
                print()
                
            