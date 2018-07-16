from PyQt5 import QtWidgets, QtSql, QtSql, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle('Список контактов')


con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con1.setDatabaseName('mydb.sqlite')
con1.open()

sqm = QtSql.QSqlQueryModel(parent=window)
# sqm.setQuery('select * from Users order by Name')
sqm.setQuery('select * from Users')

sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Имя')

window.setModel(sqm)

window.hideColumn(0)
window.setColumnWidth(1, 150)

window.resize(300, 500)
window.show()
sys.exit(app.exec_())
