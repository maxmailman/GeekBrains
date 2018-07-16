from PyQt5 import QtWidgets, QtSql, QtSql, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)

con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con1.setDatabaseName('mydb.sqlite')
con1.open()

query = QtSql.QSqlQuery()
query.exec('select * from Users good order by Name')
lst = []
if query.isActive():
    query.first()
    while query.isValid():
        lst.append(query.value('Name') + ' : ' +
                   str(query.value('UserId')) + ' счетчик ')
        query.next()
    for p in lst: print(p)
con1.close()
