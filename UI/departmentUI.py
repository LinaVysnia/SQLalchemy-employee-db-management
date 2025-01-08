from classes.departmentClass import Department
from classes.employeeClass import Employee
from modules.database import get_session as sessions
from modules.departmentLogic import *
from sqlalchemy import select

def run_add_department_UI():
    print("Adding a new department\n")
    continue_adding = True

    while continue_adding:
        while True:
            name = input(f"{"Department name": <17} ")
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
            leader = input(f"{"Department leader": <17} ")
            try: 
                leader = leader.strip().capitalize()
                if leader == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid person\n")
                continue
        
        while True:
            location = input(f"{"Location": <17} ")
            try: 
                location = location.strip().capitalize()
                if location == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid location\n")
                continue

        print(f"""
Department pending addition:
{"Name": <17} {name}
{"leader": <17} {leader}
{"location": <17} {location}
""")
        while True:
            print("\nWould you like to add this department entry to DB? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                add_department(name, leader, location)
                print("The new department entry added\n")
                input("Press enter to continue")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Department addition was cancelled")
                break

            else:
                print(f"Please make a valid selection")
        
        while True:
            print("Would you like to add another department? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                input("Adding another department\n")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Department addition ended\n")
                continue_adding = False
                break

            else:
                print(f"Please make a valid selection")


def run_update_department_UI():
    department_list = get_departments()
    if len(department_list) == 0:
        print("There are no departments in the database to be updated")
        return
    
    print("Updating departments")

    while True:
        view_departments()
        print(f"Which department (1 to {len(department_list)}) would you like to update?")
        user_choice = input("Your choice: ").strip()
        try:
            user_choice = int(user_choice) - 1 #converting user choice to index

            if user_choice not in list(range(0, len(department_list))):
                raise Exception("user choice out of range")
            
            chosen_department = department_list[user_choice]
                
            break
        except Exception as ex:
            print(ex)
            print("Invalid choice. Please try again")
            input("Press enter to continue")
    
    while True:
        print(f"\nUpdating department{chosen_department}\n")
        print(f"""Enter a corresponding number to:
    1 - update name
    2 - update leader
    3 - update location""")
        
        user_choice = input("Your choice: ").strip()

        try: 
            user_choice = int(user_choice)
            if user_choice not in list(range(1, 4)): #update this every time when adding more menu options
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
            db_department =  session.get(Department, chosen_department.id)
            db_department.name = new_name
            session.commit()

            print(f"Department name updated to {new_name}")


    if user_choice == 2:
        while True:
            new_lead = input(f"{"New department lead": <20} ")
            try: 
                new_lead = new_lead.strip().capitalize()
                if new_lead == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid leader\n")
                continue

        with sessions() as session:
            db_department =  session.get(Department, chosen_department.id)
            db_department.lead = new_lead
            session.commit()
            print(f"Deparment lead updated to {new_lead}")
        
    if user_choice == 3:
        while True:
            new_location = input(f"{"Updated location": <11} ")
            try: 
                new_location = new_location.strip().capitalize()
                if new_location == "":
                    raise Exception("Please enter something\n")
                break
            except Exception as ex:
                # print(ex)
                print("Please enter a valid location\n")
                continue

        with sessions() as session:
            db_department =  session.get(Department, chosen_department.id)
            db_department.location = new_location
            session.commit()
            print(f"Department location updated to {new_location}")
    

def run_view_departments_employees_UI():
    department_list = get_departments()

    if len(department_list) == 0:
        print("There are no departments in the database to be view")
        return
    
    print("Viewing employees in a department")

    while True:
        view_departments()
        print(f"Which department's employees (1 to {len(department_list)}) would you like to view?")
        user_choice = input("Your choice: ").strip()
        try:
            user_choice = int(user_choice) - 1 #converting user choice to index

            if user_choice not in list(range(0, len(department_list))):
                raise Exception("user choice out of range")
            
            chosen_department = department_list[user_choice]
                
            break
        except Exception as ex:
            print(ex)
            print("Invalid choice. Please try again")
            input("Press enter to continue")
    
    with sessions() as session:

        statement = select(Employee).filter(Employee.department_id == chosen_department.id)
        filtered_departments = session.execute(statement).scalars().all()

    if len(filtered_departments) != 0:
        print(f"There are {len(filtered_departments)} employee(s) in this department")
        for i, dep in enumerate(filtered_departments):
            print(f"{i+1}. {dep}")
    else:
        print("There are no employees in this department")
