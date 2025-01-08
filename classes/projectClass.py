from sqlalchemy import Column, String, Date, Boolean, Integer
from sqlalchemy.orm import relationship
from modules.project_employee import project_employee

from modules.database import Base

class Project(Base):
    __tablename__ = "projects" #only used for when the table name should be different to class name. If this was removed it would be identical to class name
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    is_active = Column(Boolean)

    def __str__(self):
        project_string=f"""
{"Name":<20} {self.name}
{"start date":<20} {self.start_date}
{"end date":<20} {self.end_date}
{"project status":<20} {("Active" if self.is_active else "Inactive")}
"""
        return project_string
    
#it's worth describing __init__ method so that you wouldn't have to call value = value

    employee = relationship("Employee", secondary=project_employee, back_populates="project")

# Projektų valdymas:
#    - Sukurkite projektų sistemą (pavadinimas, pradžios data, pabaigos data, statusas)
#    - Darbuotojai gali dirbti keliuose projektuose vienu metu (Many-to-Many ryšys)
#    - Galimybė priskirti/pašalinti darbuotojus iš projektų
#    - Galimybė peržiūrėti:
#      * Visus projekto darbuotojus
#      * Visus darbuotojo projektus