from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

a = input('Введите первое число \n')
b = input('Введите второе число \n')

s.send(a.encode())
s.send(b.encode())

sum = s.recv(1024).decode()
print('Сумма а и b с сервера равна ' + sum)
s.close()
