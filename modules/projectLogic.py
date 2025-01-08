from classes.projectClass import Project
from modules.database import get_session as sessions
from sqlalchemy import select
from datetime import date

def get_projects():
    with sessions() as session:

        projects = session.execute(select(Project)).scalars().all() #scalars() grazina tik reikiamus columns o ne visus, all() duoda sarasa is karto per kuri galesim sukti

    return projects

def add_project(name : str, start_date : date, end_date : date, status : bool):
    new_project = Project(name = name, start_date = start_date, end_date = end_date, status = status)
    with sessions() as session:
        session.add(new_project)
        session.commit()
