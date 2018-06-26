import sqlalchemy
from sqlalchemy import create_engine  # Для соединения с СУБД используется функция create_engine()
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<User('%s')>" % (self.name)


engine = create_engine('sqlite:///mydb.sqlite', echo=False, pool_recycle=7200)

Base.metadata.create_all(engine)
