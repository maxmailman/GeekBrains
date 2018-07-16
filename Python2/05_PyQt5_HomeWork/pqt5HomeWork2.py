from PyQt5 import QtCore, QtWidgets, QtSql
import sys

def addRecord():
    stm.insertRow(stm.rowCount())

def delRecord():
    stm.removeRow(tv.currentIndex().row)
    stm.select()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Список друзей')

con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con1.setDatabaseName('mydb.sqlite')
con1.open()

stm = QtSql.QSqlRelationalTableModel(parent=window)
stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
stm.setTable('Contacts')
# stm.setSort(1, QtCore.Qt.AscendingOrder)

stm.setRelation(1, QtSql.QSqlRelation('Users', 'UserId', 'Name'))
stm.setRelation(2, QtSql.QSqlRelation('Users', 'UserId', 'Name'))
stm.dataChanged.connect(stm.submitAll)
stm.select()
stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Пользователь')
stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Друг')
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
tv.setItemDelegateForColumn(1, QtSql.QSqlRelationalDelegate(tv))
tv.setItemDelegateForColumn(2, QtSql.QSqlRelationalDelegate(tv))
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 150)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton('Добавить запись')
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton('Удалить запись')
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(500, 500)
window.show()
sys.exit(app.exec_())