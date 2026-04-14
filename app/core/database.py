from app.core.config import settings
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from app.models import *
# database connection url
database_url= settings.DATABASE_URL
# create database engine
engine= create_engine(database_url,echo=True)
# create database tables
def init_db():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session