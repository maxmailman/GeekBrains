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

        self.ui.pushButton.clicked.connect(self.on_clicked_pushButton)

    def on_clicked_pushButton(self):
        print('Функция')
        message = self.ui.textEdit.append('Тест')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
