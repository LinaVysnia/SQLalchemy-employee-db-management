from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from modules.database import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    lead = Column(String(255))
    location = Column(String(255))

    def __str__(self):
        return f"""
{"name":<11} {self.name}
{"lead":<11} {self.lead}
{"location":<11} {self.location}"""
    
    employee = relationship("Employee", back_populates="department")