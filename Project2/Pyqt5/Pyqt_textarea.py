import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize


class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(650, 300))
        self.setWindowTitle("PyQt5 Пример с текстовым полем")

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("При соединении введите имя пользователя.\n")
        self.b.move(10, 10)
        self.b.resize(400, 200)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit(app.exec_())
