from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine  # Для соединения с СУБД используется функция create_engine()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'
    UserId = Column(Integer, primary_key=True)
    Name = Column(String)

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return self.Name


class Contact(Base):
    __tablename__ = 'Contacts'
    ContactId = Column(Integer, primary_key=True)
    User_1 = Column(Integer, ForeignKey('Users.UserId'))
    User_2 = Column(Integer, ForeignKey('Users.UserId'))

    def __init__(self, user_1, user_2):
        self.User_1 = user_1
        self.User_2 = user_2

    def __repr__(self):
        return '{} друг {}'.format(self.User_1, self.User_2)


engine = create_engine('sqlite:///mydb.sqlite', echo=False, pool_recycle=7200)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
print('Session: ', session)

session.add_all([User('Max'), User('Liza'), User('Misha'), User('Leo'), User('Alexandr')])
session.add_all([Contact(1, 2), Contact(2, 1), Contact(3, 1), Contact(1, 5)])

print(' ---- Все доступные пользователи ----')
q_users = session.query(User).all()
print(q_users)

print(' ---- Все контакты ----')
q_contacts = session.query(Contact).all()
print(q_contacts)

session.commit()


