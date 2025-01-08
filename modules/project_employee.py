from sqlalchemy import Table, Column, Integer, ForeignKey
from modules.database import Base

project_employee = Table(
    "project_employee",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id")),
    Column("employee_id", Integer, ForeignKey("employees.id"))
)