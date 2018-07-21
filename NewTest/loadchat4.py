from PyQt5 import QtWidgets, QtCore
import ui_chat
import sys
import socket
import threading
import time

key = 8194

shutdown = False
join = True


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))

                # Begin
                decrypt = "";
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i) ^ key)
                print(decrypt)
                # End

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0
server = (host, 7777)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = ui_chat.Ui_MainWindow()
ui.setupUi(window)
ui.textEdit.setDisabled(True)
ui.textEdit_2.setDisabled(True)
ui.pushButton.setDisabled(True)
ui.listView_2.setDisabled(True)


def on_clicked_pushButton():
    print('Функция')
    message = ui.textEdit.append(ui.textEdit_2.toPlainText())
    ui.textEdit_2.setText('')


def on_clicked_pushButLogin():
    print('Авторизация')
    login = ui.textEditLogin.toPlainText()
    if login != "":
        ui.textEditLogin.setDisabled(True)
        ui.textEdit.setDisabled(False)
        ui.textEdit_2.setDisabled(False)
        ui.pushButton.setDisabled(False)
        ui.listView_2.setDisabled(False)


ui.pushButton.clicked.connect(on_clicked_pushButton)
ui.pushButLogin.clicked.connect(on_clicked_pushButLogin)

window.show()

rT.join()

sys.exit(app.exec_())
