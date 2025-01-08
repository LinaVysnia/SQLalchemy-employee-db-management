from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import my_secrets

#dialect+driver://username:password@host:port/database
engine = create_engine(my_secrets.DB_LOGIN)

class Base(DeclarativeBase):
    pass

Sessions = sessionmaker(bind=engine)

def get_session():
    return Sessions()