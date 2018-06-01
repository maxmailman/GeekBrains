import select
from socket import *

address = ('', 8888)

# Вешаем на адрес порт
s = socket(AF_INET, SOCK_STREAM)
s.bind(address)

# Слушаем несколько клиентов
s.listen(100)
# Выставляем таймаут
s.settimeout(0.2)

# Список клиентов
# Сокеты клиентов
clients = []

# Цикл обработки
while True:
    # ждем подключения
    conn, addr = s.accept()
    # Обработка
    # Сохраняем сокет клиента в список
    clients.append(conn)
    # Обработка клиентов
    r, w, e = select.select(clients, clients, clients, 0)

    for write in r:
        # Прием сообщений
        msg = write.recv(1024)

    for reade in w:
        reade.send(b'Hello')
