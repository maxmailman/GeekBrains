import sqlalchemy
from sqlalchemy import create_engine  # Для соединения с СУБД используется функция create_engine()
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    UserId = Column(Integer, primary_key=True)
    Name = Column(String)

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return "<User('%s')>" % (self.Name)

class Contact(Base):
    __tablename__ = 'Contacts'
    ContactId = Column(Integer, primary_key=True)
    User_1 = Column(Integer, ForeignKey('Users.UserId'))
    User_2 = Column(Integer, ForeignKey('Users.UserId'))

    def __init__(self, user_1, user_2):
        self.User_1 = user_1
        self.User_2 = user_2

    def __repr__(self):
        return


engine = create_engine('sqlite:///mydb.sqlite', echo=False, pool_recycle=7200)

Base.metadata.create_all(engine)
