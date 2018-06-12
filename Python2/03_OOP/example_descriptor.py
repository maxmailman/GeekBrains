class Age:
    def __init__(self, age):
        self._age = age

    def __get__(self, obj, obgtype):
        return self._age

    def __set__(self, obj, value):
        self._age = value


class User:
    age = Age(30)
    two = 10


class Car:
    age = Age(15)


u = User()
print(u.age)
u.age = 29
print(u.age)

c = Car()
c.age = 14
print(c.age)
