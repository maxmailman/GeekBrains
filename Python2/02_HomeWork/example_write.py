from socket import *

s = socket(AF_INET, SOCK_STREAM)  # Создаем сокет ТСР
s.connect(('localhost', 9999))  # Соединяемся с сервером

while True:
    tm = s.recv(1024).decode()
    print(f'Принятое сообщение: {tm}')

s.close()
