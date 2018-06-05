import select
import time
from socket import socket, AF_INET, SOCK_STREAM


def new_listen_socket(addres):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addres)
    sock.listen(10)
    sock.settimeout(0.2)  # Таймаут для операций с сокетом
    '''таймаут небходим, чтобы не ждать появления данных в сокете'''
    return sock


def mainpool():
    '''Основной цикл обработки запросов клиента'''
    addres = ('', 8888)
    clients = []
    sock = new_listen_socket(addres)

    while True:
        try:
            conn, addr = sock.accept()  # Проверка подключений
        except OSError as e:
            pass  # таймаут вышел
        else:
            print(f'Получен запрос на соединение с {str(addr)}')
            clients.append(conn)
        finally:
            '''Проверяем наличие событий ввода-вывода без таймаута'''
            w = []
            try:
                r, w, e = select.select([], clients, [], 0)
            except Exception as e:
                # Исключение произойдет, если какой-то клиент отключится
                pass  # Ничего не делать, если какой-то клиент отключился

            # Обойти список клиентов, читающих из сокета
            '''Здесь есть вопросы по реализации try exept'''
            for s_client in w:
                timestr = time.ctime(time.time()) + '\n'
                try:
                    s_client.send(timestr.encode('utf-8'))
                except:
                    # Удаляем клиента, который отключился
                    clients.remove(s_client)


print('Эхо-сервер запущен')

mainpool()
