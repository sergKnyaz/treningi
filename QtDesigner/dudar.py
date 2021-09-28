from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("для племянников")  # заголовок (title)
        self.setGeometry(300, 250, 800, 350)  # отступы и размеры ( margins and dimensions)

        self.new_text=QtWidgets.QLabel(self)

        # создаем надпись, как пример (creating an inscription as an example)
        self.text = QtWidgets.QLabel(self)
        self.text.setText('Надпись')
        self.text.move(100, 100)
        self.text.adjustSize()  # подстраивается под размер окна

        # создаем кнопку (creating a button)
        self.bttn = QtWidgets.QPushButton(self)
        self.bttn.move(100, 150)
        self.bttn.setText('жми сюда')
        self.bttn.setFixedWidth(300)  # ширина кнопки лил чего угодно
        self.bttn.clicked.connect(self.app_bttn_label)  # при нажатии на кнопку вызывает метод

    def app_bttn_label(self):  # при нажатии на кнопку выводит текст
        self.new_text.setText(" ты нажал кнопку")
        self.new_text.move(100, 200)
        self.new_text.adjustSize()


#  функция приложения (application function)
def application():
    app = QApplication(sys.argv)  # приложение
    window = Window()  # создаем окно( creating a window)

    window.show()  # вызов окна программы (opening the program window)

    sys.exit(app.exec_())  # корректный выход из приложения (correct exit from application)


if __name__ == '__main__':  # если запускать как основной файл (if you run it as the main file)
    application()
