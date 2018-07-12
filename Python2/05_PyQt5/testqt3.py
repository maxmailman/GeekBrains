import sys

from PyQt5 import QtWidgets, uic


class MyWindows(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('unit.ui', self)

    def my_method(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindows()
    window.show()
    print(window.pushButton1)

    sys.exit(app.exec_())
