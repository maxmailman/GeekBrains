from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    msg = s.recv(1024)
    print(msg)
