from PyQt5 import QtWidgets
import sys, time


def on_clicked():
    button.setDisabled(True)  # Делаем кнопку неактивной
    for i in range(1, 21):
        QtWidgets.qApp.processEvents()  # Запускаем оборот цикла
        time.sleep(1)  # засыпаем на 1 сек
        print('step - ', i)
    button.setDisabled(False)  # Делаем кнопку активной


app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Запустить процесс')
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec_())
