from PyQt5 import QtWidgets
import sys, ui_myform

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = ui_myform.Ui_Form()
ui.setupUi(window)
ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)
window.show()
sys.exit(app.exec_())