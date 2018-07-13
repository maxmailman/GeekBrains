import sys
from PyQt5 import QtWidgets
import test_form

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = test_form.Ui_MainWindow()
ui.setupUi(window)


def hello(word):
    ui.textEdit.append(word)


def get_index():
    print(ui.comboBox.currentIndex())


try:
    class Hello:

        def __init__(self, word):
            self.word = word

        def __call__(self):
            ui.textEdit.append(self.word)


    ui.pushOk.setCheckable(True)
    ui.pushOk.clicked.connect(lambda: hello('Clicked'))
    h = Hello('Class')
    ui.pushOk.clicked.connect(h)
    ui.pushOk.clicked.connect(Hello('Clicked2'))
    ui.pushOk.clicked.connect(Hello('Clicked2'))
    # ui.pushButton.clicked.connect(app.quit)
    ui.pushOk.toggled.connect(lambda: hello('Toggled'))
    ui.pushOk.pressed.connect(lambda: hello('Pressed'))
    ui.pushOk.pressed.connect(lambda: hello('Pressed'))
    ui.pushOk.released.connect(lambda: hello('Release'))
    window.show()
    sys.exit(app.exec_())
except Exception as e:
    print(e)
