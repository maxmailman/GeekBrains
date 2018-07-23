from PyQt5 import QtWidgets, QtCore
import ui_chat
import sys
import socket
import threading
import time


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

        self.ui.pushButLogin.clicked.connect(self.on_clicked_pushButLogin)
        self.ui.pushButton.clicked.connect(self.on_clicked_pushButton)

    def on_clicked_pushButton(self):
        print('Функция')
        message = self.ui.textEdit.append(self.ui.textEdit_2.toPlainText())
        self.ui.textEdit_2.setText('')

    def on_clicked_pushButLogin(self):
        print('Авторизация')
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
