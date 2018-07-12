from PyQt5 import QtWidgets, uic
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('testform.ui', self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi('testform.ui')
    window.btnQuit.clicked.connect(app.quit)
    window.show()
    sys.exit(app.exec_())
