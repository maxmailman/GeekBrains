# Программа клиента, который запрашивает текущее время
from socket import *

s = socket(AF_INET, SOCK_STREAM)  # Создаем сокет TCP
s.connect(('localhost', 8888))  # Соединяемся с сервером
tm = s.recv(1024)  # Принимаеи не более 1024 байт данных
s.close()
print('Текущее время: %s' % tm.decode('ascii'))
print(f'Текущее время: {tm}')

# # авторизация
# s.send(b'auth my_login')
# # сообщение
# s.send(b'message hello to Max')
# # Сообщение
# s.send(b'add_to_chat')

#JIM протокол основанный на json
message = {
    'action': 'auth',
    'login': 'my_login'
    }

message = {
    'action': 'add_to_chat'
}


