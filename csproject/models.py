from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO: Add your models below this line!
class User(Base):
	__tablename__='users'
	id = Column(Integer, primary_key=True)
	full_name=Column(String)
	password=Column(String)






