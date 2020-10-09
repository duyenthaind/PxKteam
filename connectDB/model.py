from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()


def ConnectToDB():
	engine = create_engine('mysql+mysqldb://root:vjpvjp123A01@localhost/testConnectDB?charset=utf8mb4')
	Session = sessionmaker(bind=engine)
	return Session



class Name(Base):
	__tablename__ = 'name'
	id = Column(Integer, primary_key=True)
	name = Column(String)
