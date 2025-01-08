from modules.projectLogic import get_projects

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
    pass

def edit_project_UI():
    pass

def view_projects_employees_UI():
    pass

def view_employees_projects_UI():
    pass

def edit_projects_employees_UI():
    pass