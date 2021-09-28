from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_rezult = QtWidgets.QLabel(self.centralwidget)
        self.label_rezult.setGeometry(QtCore.QRect(0, 0, 350, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.label_rezult.setFont(font)
        self.label_rezult.setStyleSheet("background-color: rgb(140, 140, 140);\n"
                                        "color: rgb(255, 255, 255);")
        self.label_rezult.setObjectName("label_rezult")

        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 320, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_0.setObjectName("btn_0")

        self.btn_eqal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eqal.setGeometry(QtCore.QRect(150, 320, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_eqal.setFont(font)
        self.btn_eqal.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_eqal.setObjectName("btn_eqal")

        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 230, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 230, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 230, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_3.setObjectName("btn_3")

        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 140, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 140, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_5.setObjectName("btn_5")

        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 140, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_6.setObjectName("btn_6")

        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_7.setObjectName("btn_7")

        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 50, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_8.setObjectName("btn_8")

        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 50, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_9.setObjectName("btn_9")

        self.btn_summ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_summ.setGeometry(QtCore.QRect(300, 50, 50, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_summ.setFont(font)
        self.btn_summ.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_summ.setObjectName("btn_summ")

        self.btn_delit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delit.setGeometry(QtCore.QRect(300, 320, 50, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_delit.setFont(font)
        self.btn_delit.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_delit.setObjectName("btn_delit")

        self.btn_umnog = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umnog.setGeometry(QtCore.QRect(300, 230, 50, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_umnog.setFont(font)
        self.btn_umnog.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_umnog.setObjectName("btn_umnog")

        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(300, 140, 50, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_minus.setObjectName("btn_minus")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.app_functions()

        self.is_eqvel = False  # |||||||||||||||||

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_rezult.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_eqal.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_summ.setText(_translate("MainWindow", "+"))
        self.btn_delit.setText(_translate("MainWindow", "/"))
        self.btn_umnog.setText(_translate("MainWindow", "*"))
        self.btn_minus.setText(_translate("MainWindow", "-"))

    # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def app_functions(self):
        self.btn_0.clicked.connect(lambda: self.wrtte_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.wrtte_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.wrtte_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.wrtte_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.wrtte_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.wrtte_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.wrtte_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.wrtte_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.wrtte_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.wrtte_number(self.btn_9.text()))
        self.btn_minus.clicked.connect(lambda: self.wrtte_number(self.btn_minus.text()))
        self.btn_summ.clicked.connect(lambda: self.wrtte_number(self.btn_summ.text()))
        self.btn_delit.clicked.connect(lambda: self.wrtte_number(self.btn_delit.text()))
        self.btn_umnog.clicked.connect(lambda: self.wrtte_number(self.btn_umnog.text()))

        self.btn_eqal.clicked.connect(self.rezals)

    def wrtte_number(self, number):
        if self.label_rezult.text() == '0' or self.is_eqvel:
            self.label_rezult.setText(number)
            self.is_eqvel = False
        else:
            self.label_rezult.setText(self.label_rezult.text() + number)

    def rezals(self):
        if not self.is_eqvel:
            rez = eval(self.label_rezult.text())  # eval переводит строчный пртмер в цифровой
            self.label_rezult.setText('Резуьтат: ' + str(rez))
            self.is_eqvel = True
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Сейчас это действие выполнить нельзя')
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok | QMessageBox.Cancel)

            error.setDefaultButton((QMessageBox.Ok))  # подсветка кнопки на экране
            error.setInformativeText('Два раза действие не выполняется')
            error.setDetailedText('Детали')

            error.buttonClicked.connect(self.popup_action)

            error.exec_()  # выводим на экран

    def popup_action(self, btn):
        if btn.text() == 'Ok':
            print('Print Ok')
        elif btn.text() == 'Reset':
            self.label_rezult.setText("")
            self.is_eqvel = False


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
