from sqlalchemy import Column, Integer, String, Date, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base #do i need this?
from sqlalchemy.orm import relationship
from modules.project_employee import project_employee

from modules.database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    surname = Column(String(32))
    role = Column(String(32))
    salary = Column(Integer, nullable=False)
    start_date = Column(Date) #would be nice to add an option to add a different start date
    # start_date = Column(Date, server_default= func.now()) #func now breaks alembic
    department_id = Column(Integer, ForeignKey("departments.id"))

    def __str__(self):
        return_string = f"""
{"name":<20} {self.name}
{"surname":<20} {self.surname}
{"role":<20} {self.role}
{"salary":<20} {self.salary}
{"start date":<20} {self.start_date}
"""
#{"department name":<20} {self.department.name} veikia nebent jei kvieciame vienoje sesijoje
        return return_string
    
    department = relationship("Department", back_populates="employee")
    project = relationship("Project", secondary=project_employee, back_populates="employee")