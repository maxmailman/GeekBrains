class Age:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

class User:
    def __init__(self, age):
        self._age = age

class Car:
    def __init__(self, age):
        self._age = age


age = Age(30)
u = User(age)

age = Age(15)
c = Car(age)

print(c._age.age)
