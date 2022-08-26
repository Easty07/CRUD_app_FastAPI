from sqlalchemy import Column, Integer, String
from database import Base


# Define Item class inheriting from Base
class Item(Base):
    __tablename__ = 'students_app'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
    # first_name = Column(String)