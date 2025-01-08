from modules.database import Base, engine
from classes.employeeClass import Employee
from classes.departmentClass import Department
from classes.projectClass import Project

# Base.metadata.create_all(bind=engine)

#init file is run when something is imported from the folder that it's at. 
#This current use is incorrect because every time something is imported, the tables are "created". It should be in another file and be run when the program starts