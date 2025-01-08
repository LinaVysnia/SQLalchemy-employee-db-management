from modules.projectLogic import get_projects
from modules.database import get_session
from modules.projectLogic import add_project
from classes.projectClass import Project
from datetime import datetime

def view_projects():
    projects = get_projects()

    if projects:
        print(f"{len(projects)} project(s) found\n")
        i = 1
        for project in projects:
            print(f"{i}. {project}")
            i += 1
    else:
        print("There are no projects in the database\n")

def add_project_UI():
    print("Adding a new project\n")
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
                print("Please enter a valid project name\n")
                continue
        
        continue_asking_for_start_date = True
        while continue_asking_for_start_date:

            print("\nWould you like to specify project start date? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":

                while True:
                    start_date_string = input(f"{"Start date (YYYY MM DD): " : <11} ")
                    try: 
                        start_date = datetime.strptime(start_date_string, "%Y %m %d").date()
                        if start_date.year < 1900 or start_date.year > 2100:
                            raise Exception("Invalid date\n")
                        
                        continue_asking_for_start_date = False
                        break
                    except Exception as ex:
                        # print(ex)
                        print("Please enter a valid date (YYYY MM DD)\n")
                        continue

                # input("Press enter to continue")
                # break

            elif user_choice == "no" or user_choice == "n":
                start_date = None
                continue_asking_for_start_date - False
                break

            else:
                print(f"Please make a valid selection")

        continue_asking_for_end_date = True
        while continue_asking_for_end_date:

            print("\nWould you like to specify project end date? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":

                while True:
                    end_date_string = input(f"{"End date (YYYY MM DD): " : <11} ")
                    try: 
                        end_date = datetime.strptime(end_date_string, "%Y %m %d").date()

                        if start_date != None:
                            if end_date < start_date:
                                print("End date can't be earlier than the start date")
                                raise Exception("Invalid date\n")

                        if end_date.year < 1900 or end_date.year > 2100:
                            raise Exception("Invalid date\n")
                        
                        continue_asking_for_end_date = False
                        break
                    except Exception as ex:
                        print(ex)
                        print("Please enter a valid date (YYYY MM DD)\n")
                        continue

            elif user_choice == "no" or user_choice == "n":
                end_date = None
                continue_asking_for_end_date - False
                break

            else:
                print(f"Please make a valid selection")

        while True:
            status_str = input(f"{"Status (Active/Inactive): " : <11} ").strip().capitalize()
            if status_str == "Active" or status_str == "A":
                status = 1
                break
            elif status_str == "Inactive" or status_str == "I":
                status = 0
                break
            else:
                print("Invalid selection! Please enter 'Active' or 'Inactive'")

        print(f"""
Project pending addition:
{"Name": <15} {name}
{"Start date": <15} {start_date}
{"End date": <15} {end_date}
{"Project status": <15} {("Active" if status else "Inactive")} 
""")
        while True:
            print("\nWould you like to add this project entry to DB? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                add_project(name, start_date, end_date, status)
                print("The new project entry added\n")
                input("Press enter to continue")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Project addition was cancelled")
                break

            else:
                print(f"Please make a valid selection")
        
        while True:
            print("Would you like to add another project? (y/n)")
            user_choice = input("Your choice: ").strip().lower()

            if user_choice == "yes" or user_choice == "y":
                print("Adding another project\n")
                input("Press enter to continue")
                break

            elif user_choice == "no" or user_choice == "n":
                print("Project addition ended\n")
                continue_adding = False
                break

            else:
                print(f"Please make a valid selection")

def edit_project_UI():
    project_list = get_projects()
    if len(project_list) == 0:
        print("There are no projects in the database to be updated")
        return
    
    print("Updating projects")
    while True:
        view_projects()
        print(f"Which project (1 to {len(project_list)}) would you like to update?")
        user_choice = input("Your choice: ").strip()
        try:
            user_choice = int(user_choice) - 1 #converting user choice to index

            if user_choice not in list(range(0, len(project_list))):
                raise Exception("user choice out of range")
            
            chosen_project = project_list[user_choice][0]
            chosen_project : Project

            break
        except Exception as ex:
            print(ex)
            print("Invalid choice. Please try again")
            input("Press enter to continue")

    while True:
        print(f"\nUpdating project{chosen_project}\n")
        print(f"""Enter a corresponding number to:
    1 - update name
    2 - update start date
    3 - update end date
    4 - update status
""")    

        user_choice = input("Your choice: ").strip()

        try: 
            user_choice = int(user_choice)
            if user_choice not in list(range(1, 5)): #update this every time when adding more menu options
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

        with get_session() as session:
            db_employee =  session.get(Employee, chosen_employee.id)
            db_employee.name = new_name
            session.commit()

            print(f"Employee name updated to {new_name}")            
def view_projects_employees_UI():
    pass

def view_employees_projects_UI():
    pass

def edit_projects_employees_UI():
    pass