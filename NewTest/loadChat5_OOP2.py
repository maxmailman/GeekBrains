from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
import ui_chat
import sys
import socket
import time


class Thread1(QtCore.QThread):
    s1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.exec_()  # Запускаем цикл обработки сигналов
        # self.s1.emit('Привет, я поток 1')

    def on_change(self):
        for step in range(100):
            time.sleep(0.1)
            self.s1.emit('Привет, я поток 1')
        self.s


class Worker(QObject):
    sig_msg = pyqtSignal(str)

    # def __init__(self):
    #     super().__init__()

    @pyqtSlot()
    def work(self):
        for step in range(100):
            time.sleep(0.1)
            self.sig_msg.emit('step ' + str(step))


class MyThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        print('Старт потока')


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

        self.myThread = MyThread()
        self.myThread.start()

        # self.ui.thread1 = Thread1()
        # self.ui.thread1.start()

        self.ui.pushButLogin.clicked.connect(self.on_clicked_pushButLogin)
        # self.ui.pushButton.clicked.connect(self.ui.thread1.on_change)

        # self.ui.thread1.s1.connect(self.on_clicked_pushButton, QtCore.Qt.QueuedConnection)

    def on_clicked_pushButLogin(self):
        # print('Авторизация')
        login = self.ui.textEditLogin.toPlainText()
        if login != "":
            self.ui.pushButLogin.setDisabled(True)
            self.ui.textEditLogin.setDisabled(True)
            self.ui.textEdit.setDisabled(False)
            self.ui.textEdit_2.setDisabled(False)
            self.ui.pushButton.setDisabled(False)
            # self.ui.listView_2.setDisabled(False)
            self.myThread.isRunning()

    def on_clicked_pushButton(self, i):
        print('Отправить в текст')
        self.ui.textEdit.append(i)
        self.ui.textEdit_2.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
