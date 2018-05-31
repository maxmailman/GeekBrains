from socket import *

from decode import Decode
from decode import Encode_send_sum

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(10)

while True:
    client, addr = s.accept()
    print(f'Присоединение клиента {addr}')

    a = Decode(client.recv(1024)).get_dec
    b = Decode(client.recv(1024)).get_dec

    print('Отправляем сумму чисел на клиент')
    client.send(Encode_send_sum(a).get_sum_en(b))

    client.close()
