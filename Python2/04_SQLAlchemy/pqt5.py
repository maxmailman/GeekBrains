from PyQt5 import QtWidgets, QtSql, QtSql, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)

con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con1.setDatabaseName('mydb.sqlite')
con1.open()
if 'Users' in con1.tables():
    print('Таблица есть!')
con1.close()
