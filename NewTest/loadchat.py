from PyQt5 import QtWidgets
import ui_chat
import sys


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui_chat.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
