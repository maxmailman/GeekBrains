from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    msg = input('Введите сообщение')
    msg = s.send(msg)
