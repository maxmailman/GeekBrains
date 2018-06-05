from socket import *

s = socket(AF_INET, SOCK_STREAM)  # Создаем сокет ТСР
s.connect(('localhost', 8888))  # Соединяемся с сервером

while True:
    tm = s.recv(1024)
    print(f'Текущее время: {tm}')

s.close()
