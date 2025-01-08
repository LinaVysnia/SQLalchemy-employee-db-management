from modules.employeeLogic import *
from classes.employeeClass import Employee
from classes.departmentClass import Department
from modules.database import get_session as sessions
from datetime import datetime

def run_add_employee_UI():
    print("Adding a new employee\n")
    continue_adding = True

    while continue_adding:
        while True:
            name = input(f"{"Name": <11} ")
            try: 
                name = name.strip().capitalize()
                if name == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                print(ex)
                print("Please enter a valid name\n")
                continue

        while True:
            surname = input(f"{"Surname": <11} ")
            try: 
                surname = surname.strip().capitalize()
                if surname == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid surname\n")
                continue
        
        while True:
            role = input(f"{"Role": <11} ")
            try: 
                role = role.strip().capitalize()
                if role == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid role\n")
                continue
            
        while True:
            salary = input(f"{"Salary" : <11} ")
            try: 
                salary = int(salary.strip())
                if salary < 0:
                    raise Exception("Invalid salary\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid salary\n")
                continue
        
        while True:
            start_date_string = input(f"{"Start date (YYYY MM DD): " : <11} ")
            try: 
                start_date = datetime.strptime(start_date_string, "%Y %m %d").date()
                if start_date.year < 1900 or start_date.year > 2100:
                    raise Exception("Invalid date\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid date (YYYY MM DD)\n")
                continue


        with sessions() as session:
            all_departments = session.execute(select(Department)).fetchall()

        if not all_departments:
            print("There are no departments to assign to the employee. Please add more departments before assigning them")
            department = None
            
        else:
            print(f"{len(all_departments)} available department(s) found\n")
            # print(all_departments)
            i = 1
            for department in all_departments:
                print(f"{i}. {department[0].name}")
                i += 1

            print(f"{i}. Keep department unassigned")

            while True:
                print(f"\nNew department number (from 1 to {i}): ")
                department_num = input("Your choice: ")

                try:
                    department_num = int(department_num.strip())

                    if department_num not in list(range(1, (i + 1))):
                        raise Exception("Invalid department\n")
                    break

                except Exception as ex:
                    # print(ex)
                    print("Please enter a valid number\n")
                    continue
            
            if department_num == i:
                department = None

            else:
                department = all_departments[department_num - 1][0]

        print(f"""
Employee pending addition:
{"Name": <11} {name}
{"Surname": <11} {surname}
{"Role": <11} {role}
{"Salary": <11} {salary} 
{"Start date": <11} {start_date_string} 
{"Department": <11} {department or "unassigned"} 
""")
        while True:
            print("\nWould you like to add this employee entry to DB? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                add_employee(name, surname, role, salary, start_date, department)
                print("The new employee entry added\n")
                input("Press enter to continue")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Employee addition was cancelled")
                break

            else:
                print(f"Please make a valid selection")
        
        while True:
            print("Would you like to add another employee? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                input("Adding another employee\n")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Employee addition ended\n")
                continue_adding = False
                break

            else:
                print(f"Please make a valid selection")

def run_update_employee_UI():
    employee_list = get_employees()
    if len(employee_list) == 0:
        print("There are no employees in the database to be updated")
        return
    
    print("Updating employees")

    while True:
        view_employees()
        print(f"Which employee (1 to {len(employee_list)}) would you like to update?")
        user_choice = input("Your choice: ").strip()
        try:
            user_choice = int(user_choice) - 1 #converting user choice to index

            if user_choice not in list(range(0, len(employee_list))):
                raise Exception("user choice out of range")
            
            chosen_employee = employee_list[user_choice][0]
            chosen_employee : Employee

            #handling the cases when employee doesnt have a department
            if employee_list[user_choice][1] != None:
                old_department_name = employee_list[user_choice][1].name
            else:
                old_department_name = "unassigned"
                
            break
        except Exception as ex:
            print(ex)
            print("Invalid choice. Please try again")
            input("Press enter to continue")
    
    while True:
        print(f"\nUpdating employee{chosen_employee}{"Department" :<20} {old_department_name}\n")
        print(f"""Enter a corresponding number to:
    1 - update name
    2 - update surname
    3 - update role
    4 - update salary
    5 - update start date
    6 - update department""")
        
        user_choice = input("Your choice: ").strip()

        try: 
            user_choice = int(user_choice)
            if user_choice not in list(range(1, 7)): #update this every time when adding more menu options
                raise Exception
            break

        except:
            print("Invalid choice")
    
    if user_choice == 1:
        while True:
            new_name = input(f"{"Updated name": <11} ")
            try: 
                new_name = new_name.strip().capitalize()
                if new_name == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                print(ex)
                print("Please enter a valid name\n")
                continue

        with sessions() as session:
            db_employee =  session.get(Employee, chosen_employee.id)
            db_employee.name = new_name
            session.commit()

            print(f"Employee name updated to {new_name}")


    if user_choice == 2:
        while True:
            new_surname = input(f"{"Updated surname": <11} ")
            try: 
                new_surname = new_surname.strip().capitalize()
                if new_surname == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid surname\n")
                continue

        with sessions() as session:
            db_employee =  session.get(Employee, chosen_employee.id)
            db_employee.surname = new_surname
            session.commit()
            print(f"Employee surname updated to {new_surname}")
        
    if user_choice == 3:
        while True:
            new_role = input(f"{"Updated role": <11} ")
            try: 
                new_role = new_role.strip().capitalize()
                if new_role == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid role\n")
                continue

        with sessions() as session:
            db_employee =  session.get(Employee, chosen_employee.id)
            db_employee.role = new_role
            session.commit()
            print(f"Employee role updated to {new_role}")
            
    if user_choice == 4:
        while True:
            new_salary = input(f"{"Updated salary" : <11} ")
            try: 
                new_salary = int(new_salary.strip())
                if new_salary < 0:
                    raise Exception("Invalid salary\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid salary\n")
                continue

        with sessions() as session:
            db_employee =  session.get(Employee, chosen_employee.id)
            db_employee.salary = new_salary
            session.commit()
            print(f"Employee salary updated to {new_salary}")

    if user_choice == 5:

        while True:
            new_start_date_string = input(f"{"New start date (YYYY MM DD):" : <11} ")
            try: 
                new_start_date = datetime.strptime(new_start_date_string, "%Y %m %d").date()
                if new_start_date.year < 1900 or new_start_date.year > 2100:
                    raise Exception("Invalid date\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid date (format YYYY MM DD)\n")
                continue

        with sessions() as session:
            db_employee =  session.get(Employee, chosen_employee.id)
            db_employee.start_date = new_start_date
            session.commit()
            print(f"Employee start date updated to {new_start_date_string}")

    if user_choice == 6:

        with sessions() as session:
            all_departments = session.execute(select(Department)).fetchall()

        if not all_departments:
            print("There are no departments to assign to the employee. Please add more departments before assigning them")
            
        else:
            print(f"{len(all_departments)} available department(s) found\n")
            # print(all_departments)
            i = 1
            for department in all_departments:
                print(f"{i}. {department[0].name}")
                i += 1

            while True:
                print(f"\nNew department number (from 1 to {len(all_departments)}): ")
                new_department_num = input("Your choice: ")

                try: 
                    new_department_num = int(new_department_num.strip()) - 1

                    if new_department_num not in list(range(0, len(all_departments))):
                        raise Exception("Invalid department\n")
                    break

                except Exception as ex:
                    # print(ex)
                    print("Please enter a valid department number\n")
                    continue
                
            new_department = all_departments[new_department_num][0]

            with sessions() as session:
                db_employee =  session.get(Employee, chosen_employee.id)
                db_employee.department_id = new_department.id
                session.commit()

                print(f"Employee department updated from {old_department_name} to {new_department.name}")

def run_delete_employee_UI():
   employee_list = get_employees()
   continue_deleting = True

   while continue_deleting :
        
        view_employees()
        print(f"Which employee (1 to {len(employee_list)}) would you like to delete?")
        user_choice = input("Your choice: ").strip()
        try:
            user_choice = int(user_choice) - 1
            if user_choice not in list(range(0, len(employee_list))):
                raise Exception
            
            chosen_employee = employee_list[user_choice]
        except:
            print("Invalid choice. Please try again")
            input("Press enter to continue")
            continue
        
        print(f"Employee chosen for deletion: {chosen_employee}")

        while True:
            print("\nAre you sure you want to delete? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                with sessions() as session:
                    db_employee =  session.get(Employee, chosen_employee.id)
                    session.delete(db_employee)
                    session.commit()

                print(f"Deleted employee {chosen_employee}")
                input("Press enter to continue")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Employee deletion was cancelled")
                break

            else:
                print(f"Please make a valid selection")

        while True:
            print("Would you like to delete another employee? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                print("Deleting another employee\n")
                input("Press enter to continue")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Employee addition ended\n")
                continue_deleting = False
                break

            else:
                print(f"Please make a valid selection")