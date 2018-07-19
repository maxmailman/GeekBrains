#Программа сервера времени
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)    # Создаем сокет TCP
s.bind(('', 8888))                  # Присваем порт 8888
s.listen(5)                         # Переходим в режим ожидания запросов, в данном случае не больше 5

while True:
    client, addr = s.accept()       # Принимаем запрос на соединение
    print('Получен запрос на соединение от %s' % str(addr))
    timestr = time.ctime(time.time()) + '\n'
    client.send(timestr.encode('ascii'))
    client.close()