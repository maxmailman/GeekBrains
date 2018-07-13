from PyQt5 import QtWidgets

import MyWindow


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.myWidget = MyWindow.MyWindow()
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)
        self.button = QtWidgets.QPushButton('Изменить надпись')
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText('Новая запись')
        self.button.setDisabled(True)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    windows = MyDialog()
    windows.setWindowTitle("Преимущество ООП-стиля")
    windows.resize(300, 100)
    windows.show()
    sys.exit(app.exec_())
