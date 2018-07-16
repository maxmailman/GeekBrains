from PyQt5 import QtCore, QtWidgets, QtSql
import sys

def addRecord():
    stm.insertRow(stm.rowCount())

def delRecord():
    stm.removeRow(tv.currentIndex().row)
    stm.select()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Список контактов')

con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con1.setDatabaseName('mydb.sqlite')
con1.open()

stm = QtSql.QSqlTableModel(parent=window)
stm.setTable('Users')
# stm.setSort(1, QtCore.Qt.AscendingOrder)
stm.select()

stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Имя')

vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton('Добавить запись')
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton('Удалить запись')
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(300, 500)
window.show()
sys.exit(app.exec_())