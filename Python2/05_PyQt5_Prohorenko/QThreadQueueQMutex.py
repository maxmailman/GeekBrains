from PyQt5 import QtCore, QtWidgets


class MyThread(QtCore.QThread):
    x = 10  # Атрибут класса
    mutex = QtCore.QMutex()  # Мьютекс

    def __init__(self, id, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id

    def run(self):
        self.change_x()

    def change_x(self):
        MyThread.mutex.lock()  # Блокируем
        print('x = ', MyThread.x, " id = ", self.id)
        MyThread.x += 5
        self.sleep(2)
        print('x = ', MyThread.x, " id = ", self.id)
        MyThread.mutex.unlock()  # Снимаем блокировку


class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText('ЗАпустить')
        self.thread1 = MyThread(1)
        self.thread2 = MyThread(2)
        self.clicked.connect(self.on_start)

    def on_start(self):
        if not self.thread1.isRunning(): self.thread1.start()
        if not self.thread2.isRunning(): self.thread2.start()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Использование Mutex')
    window.resize(300, 30)
    window.show()
    sys.exit(app.exec_())
