class RevealAccess(object):
    """Дескриптор данных, который устанавливает и возвращает значения,
       и печатает сообщение о том, что к атрибуту был доступ.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print
        'Получаю', self.name
        return self.val

    def __set__(self, obj, val):
        print
        'Обновляю', self.name
        self.val = val
