from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# TODO: Add your database functions below this line!
def createU(full_name,password):
	user1=User(full_name=full_name,password=password)
	session.add(user1)
	session.commit()

def query_all():
	return session.query(User).all()

def	user_by_username(username):
	return session.query(User).filter_by(username=username).first()




