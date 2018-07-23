from PyQt5 import QtWidgets, QtCore
import ui_chat
import sys
import socket
import threading
import time

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = ui_chat.Ui_MainWindow()
ui.setupUi(window)


def on_clicked_pushButton():
    print('Функция')
    message = ui.textEdit.append(ui.textEdit_2.toPlainText())
    ui.textEdit_2.setText('')


ui.pushButton.clicked.connect(on_clicked_pushButton)

window.show()
sys.exit(app.exec_())
