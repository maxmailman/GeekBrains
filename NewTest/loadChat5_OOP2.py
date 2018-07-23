from PyQt5 import QtWidgets, QtCore
import ui_chat
import sys
import socket
import time


class Thread1(QtCore.QThread):
    s1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        # self.exec_()  # Запускаем цикл обработки сигналов
        self.s1.emit('Привет, я поток 1')

    # def on_change(self):
    #     self.s1.emit('Привет, я поток 1')
    #     # self.sleep(1)
    #     # window.ui.textEdit.append('Привет, я поток 1')


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui_chat.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEditLogin.setDisabled(False)
        self.ui.textEdit.setDisabled(True)
        self.ui.textEdit_2.setDisabled(True)
        self.ui.pushButton.setDisabled(True)
        self.ui.listView_2.setDisabled(True)

        self.ui.thread1 = Thread1()
        self.ui.thread1.start()

        self.ui.pushButLogin.clicked.connect(self.on_clicked_pushButLogin)
        self.ui.pushButton.clicked.connect(self.ui.thread1.run)

        self.ui.thread1.s1.connect(self.on_clicked_pushButton, QtCore.Qt.QueuedConnection)

    def on_clicked_pushButLogin(self):
        # print('Авторизация')
        login = self.ui.textEditLogin.toPlainText()
        if login != "":
            self.ui.textEditLogin.setDisabled(True)
            self.ui.textEdit.setDisabled(False)
            self.ui.textEdit_2.setDisabled(False)
            self.ui.pushButton.setDisabled(False)
            self.ui.listView_2.setDisabled(False)

    def on_clicked_pushButton(self, i):
        print('Отправить в текст')
        self.ui.textEdit.append(i)
        self.ui.textEdit_2.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
