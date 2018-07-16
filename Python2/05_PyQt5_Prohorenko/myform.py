from PyQt5 import uic, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('MyForm.ui')
window.btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())

