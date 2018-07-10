from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('unit.ui')
window.show()
print(window.pushButton1)

sys.exit(app.exec_())