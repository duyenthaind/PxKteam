from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()


# khoi tao ket noi vao co so du lieu
def ConnectToDB():
	engine = create_engine('mysql+mysqldb://root:vjpvjp123A01@localhost/test1_crawlData_DesignAgain?charset=utf8mb4')
	Session = sessionmaker(bind=engine)
	return Session

class Apartments(Base):
	__tablename__ = 'apartments'
