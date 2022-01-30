import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)


def window():
    app = QApplication(sys.argv)
    login = Login()
    widget = QStackedWidget()
    widget.addWidget(login)
    widget.setFixedHeight(300)
    widget.setFixedWidth(450)
    widget.show()

    try:
        sys.exit(app.exec())
    except:
        print("Exiting....")


if __name__ == '__main__':
    window()
