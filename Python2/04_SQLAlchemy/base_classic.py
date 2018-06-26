import sqlalchemy
from sqlalchemy import create_engine  # Для соединения с СУБД используется функция create_engine()
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper

print("Версия SQLAlchemy:", sqlalchemy.__version__)  # посмотреть версию SQLALchemy
engine = create_engine('sqlite:///mydb.sqlite', echo=True, pool_recycle=7200)

metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50))
                    )

metadata.create_all(engine)


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<User ('%s')>" % self.name


mapper(User, users_table)
user = User('Max')
print(user)
print(user.id)