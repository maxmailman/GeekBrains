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
        self.count = 'Привет, я поток1'
        self.s1.emit(self.count)


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
        self.ui.thread1.started.connect(self.on_clicked_pushButLogin)
        self.ui.thread1.s1.connect(self.on_clicked_pushButton, QtCore.Qt.QueuedConnection)

        self.ui.pushButLogin.clicked.connect(self.on_clicked_pushButLogin)
        self.ui.pushButLogin.clicked.connect(self.ui.thread1.run)

    def on_clicked_pushButton(self, i):
        print('Отправить в текст')
        self.ui.textEdit.append(i)
        self.ui.textEdit_2.setText('')

    def on_clicked_pushButLogin(self):
        # print('Авторизация')
        login = self.ui.textEditLogin.toPlainText()
        if login != "":
            self.ui.textEditLogin.setDisabled(True)
            self.ui.textEdit.setDisabled(False)
            self.ui.textEdit_2.setDisabled(False)
            self.ui.pushButton.setDisabled(False)
            self.ui.listView_2.setDisabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
