# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\server_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.welcome_widget = QtWidgets.QWidget(Dialog)
        self.welcome_widget.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.welcome_widget.setStyleSheet("")
        self.welcome_widget.setObjectName("welcome_widget")
        self.server_ip = QtWidgets.QLineEdit(self.welcome_widget)
        self.server_ip.setGeometry(QtCore.QRect(110, 160, 201, 21))
        self.server_ip.setStyleSheet("    text-transform: capitalize;\n"
"    font: 12pt \"MS Reference Sans Serif\";\n"
"    width: 100%;\n"
"    box-sizing: border-box;\n"
"    outline: none;\n"
"    border: none;\n"
"    border-bottom: 1px solid #000000;\n"
"    color: #07315B;\n"
"    background-color:transparent;")
        self.server_ip.setObjectName("server_ip")
        self.enter_page = QtWidgets.QLabel(self.welcome_widget)
        self.enter_page.setGeometry(QtCore.QRect(110, 100, 191, 31))
        self.enter_page.setStyleSheet("\n"
"font: 75 20pt \"MS Serif\";\n"
"color: black;")
        self.enter_page.setObjectName("enter_page")
        self.login = QtWidgets.QPushButton(self.welcome_widget)
        self.login.setGeometry(QtCore.QRect(130, 250, 151, 31))
        self.login.setStyleSheet("border-style: outset;\n"
"border-width: 3px;\n"
"font:  8pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"background-color: rgb(185, 246, 255);\n"
"")
        self.login.setObjectName("login")
        self.error = QtWidgets.QLabel(self.welcome_widget)
        self.error.setGeometry(QtCore.QRect(110, 190, 201, 51))
        self.error.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 10pt \"Yu Gothic\";")
        self.error.setText("")
        self.error.setObjectName("error")
        self.label = QtWidgets.QLabel(self.welcome_widget)
        self.label.setGeometry(QtCore.QRect(80, 60, 271, 41))
        self.label.setStyleSheet("\n"
"font: 75 20pt \"MS Serif\";\n"
"color: black;")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.enter_page.setText(_translate("Dialog", "Enter Server IP"))
        self.login.setText(_translate("Dialog", "Log In"))
        self.label.setText(_translate("Dialog", "WELCOME TO PING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

