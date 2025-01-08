from classes.employeeClass import Employee
from classes.departmentClass import Department
from modules.database import get_session as sessions
from sqlalchemy import select

def get_employees():
    """Gets info from db about employees and departments returns them in a tuple

    Returns:
        tuple : [0] employee info list [1] depatment info list
    """    

    with sessions() as session:

        statement = select(Employee, Department).join(Department, Employee.department_id == Department.id, isouter=True)
        employee_department_raw = session.execute(statement)
        employee_department_result = list(employee_department_raw)

    return employee_department_result #returns touples or employees
    
def view_employees():
    employee_info = get_employees()

    if employee_info:

        print(f"{len(employee_info)} employee(s) found\n")
        i = 1
        for employee, department in employee_info:
            if department != None:
                print(f"{i}. {employee}{"Department" :<20} {department.name} (Lead {department.lead}. Located {department.location})\n")
            else:
                print(f"{i}. {employee}{"Department" :<20} unassigned\n")
            i += 1
    else:
        print("There are no employees in the database\n")

def add_employee(name : str, surname : str, role : str, salary : int, start_date, department):
    new_employee = Employee(name = name, surname = surname, role = role, salary = salary, start_date=start_date, department=department)
    with sessions() as session:
        session.add(new_employee)
        session.commit()

