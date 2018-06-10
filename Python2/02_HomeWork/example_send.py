from socket import *

s = socket(AF_INET, SOCK_STREAM)  # Создаем сокет ТСР
s.connect(('localhost', 9999))  # Соединяемся с сервером

while True:
    tm = input('Введите сообщение \n').encode()
    s.send(tm)

s.close()
