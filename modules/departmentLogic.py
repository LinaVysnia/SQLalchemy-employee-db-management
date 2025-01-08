from classes.departmentClass import Department
from modules.database import get_session as sessions
from sqlalchemy import select

def get_departments():
    # session = sessions()
    with sessions() as session:
        statement = select(Department)
        departments = session.execute(statement).scalars().all()
        return departments
    
def view_departments():
    departments = get_departments()
    if departments:
        print(f"{len(departments)} department(s) found\n")
        i = 1
        for department in departments:
            print(f"{i}. {department}")
            i += 1
    else:
        print("There are no departments in the database\n")

def add_department(name : str, lead : str, location : str):
    new_department = Department(name = name, lead = lead, location = location)
    with sessions() as session:
        session.add(new_department)
        session.commit()

