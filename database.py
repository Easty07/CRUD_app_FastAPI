from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#create database engine
engine = create_engine('sqlite:///Studentapp.db')

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, bind=engine)