from modules.projectLogic import get_projects
from modules.database import get_session
from modules.projectLogic import add_project
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
    pass

def view_projects_employees_UI():
    pass

def view_employees_projects_UI():
    pass

def edit_projects_employees_UI():
    pass