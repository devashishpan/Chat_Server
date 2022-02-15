# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 301)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 451, 301))
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color :qlineargradient(spread:pad, x1:0.19346, y1:0.233, x2:1, y2:1, "
                                  "stop:0 rgba(255, 128, 238, 255), stop:1 rgba(255, 255, 255, 255))\n "
                                  "}\n"
                                  "")
        self.widget.setObjectName("widget")
        self.welcome = QtWidgets.QLabel(self.widget)
        self.welcome.setGeometry(QtCore.QRect(170, 40, 101, 31))
        self.welcome.setStyleSheet("\n"
                                   "font: 75 20pt \"MS Serif\";\n"
                                   "color: white;")
        self.welcome.setObjectName("welcome")
        self.signin = QtWidgets.QLabel(self.widget)
        self.signin.setGeometry(QtCore.QRect(120, 80, 221, 21))
        self.signin.setStyleSheet("font: 63 9pt \"Lucida Sans Typewriter\";\n"
                                  "color: white;")
        self.signin.setObjectName("signin")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(150, 250, 151, 31))
        self.login.setStyleSheet("border-style: outset;\n"
                                 "border-width: 3px;\n"
                                 "font:  8pt \"Arial Black\";\n"
                                 "border-radius: 10px;\n"
                                 "border-color: beige;\n"
                                 "background-color: rgb(185, 246, 255);\n"
                                 "")
        self.login.setObjectName("login")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(130, 130, 201, 21))
        self.username.setStyleSheet("    text-transform: capitalize;\n"
                                    "    font: 12pt \"MS Reference Sans Serif\";\n"
                                    "    width: 100%;\n"
                                    "    box-sizing: border-box;\n"
                                    "    outline: none;\n"
                                    "    border: none;\n"
                                    "    border-bottom: 1px solid #000000;\n"
                                    "    color: #07315B;\n"
                                    "    background-color:transparent;")
        self.username.setObjectName("username")
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setGeometry(QtCore.QRect(130, 110, 51, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 47, 13))
        self.label_2.setObjectName("label_2")
        self.error = QtWidgets.QLabel(self.widget)
        self.error.setGeometry(QtCore.QRect(130, 220, 201, 16))
        self.error.setStyleSheet("color: rgb(255, 0, 0);\n"
                                 "font: 75 10pt \"Yu Gothic\";")
        self.error.setText("")
        self.error.setObjectName("error")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(130, 190, 201, 21))
        self.password.setStyleSheet("    text-transform: capitalize;\n"
                                    "    font: 12pt \"MS Reference Sans Serif\";\n"
                                    "    width: 100%;\n"
                                    "    box-sizing: border-box;\n"
                                    "    outline: none;\n"
                                    "    border: none;\n"
                                    "    border-bottom: 1px solid #000000;\n"
                                    "    color: #07315B;\n"
                                    "    background-color:transparent;")
        self.password.setObjectName("password")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome.setText(_translate("Dialog", "LOG IN"))
        self.signin.setText(_translate("Dialog", "Sign in to Your Existing Account"))
        self.login.setText(_translate("Dialog", "Log In"))
        self.label_1.setText(_translate("Dialog", "User Name"))
        self.label_2.setText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
