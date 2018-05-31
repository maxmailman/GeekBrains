# Программа сервера времени
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)  # Создание сокета TCP
s.bind(('', 8888))  # Присваиваем порт 8888
s.listen(5)  # Переходим в режим ожидания запросов, одновременно слушаем не более 5 запросов (не более 5 соединений)

while True:
    client, addr = s.accept()  # Принимаем запрос на соединение
    print('Получен запрос на соединение от %s' % str(addr))
    timestr = time.ctime(time.time()) + '\n'

    # Далее ведем работу с сокетом клиента
    client.send(timestr.encode('ascii'))  # Передаем байты, кодируя строку в ascii
    client.close()