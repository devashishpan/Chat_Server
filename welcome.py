# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
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
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 30, 271, 41))
        self.label.setStyleSheet("\n"
                                 "font: 75 20pt \"MS Serif\";\n"
                                 "color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(120, 80, 221, 21))
        self.label_2.setStyleSheet("font: 63 9pt \"Lucida Sans Typewriter\";\n"
                                   "color: white;")
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(150, 130, 151, 31))
        self.login.setStyleSheet("border-style: outset;\n"
                                 "border-width: 3px;\n"
                                 "font:  8pt \"Arial Black\";\n"
                                 "border-radius: 10px;\n"
                                 "border-color: beige;\n"
                                 "background-color: rgb(185, 246, 255);\n"
                                 "")
        self.login.setObjectName("login")
        self.create_acc = QtWidgets.QPushButton(self.widget)
        self.create_acc.setGeometry(QtCore.QRect(150, 190, 151, 31))
        self.create_acc.setStyleSheet("border-style: outset;\n"
                                      "border-width: 3px;\n"
                                      "font:  8pt \"Arial Black\";\n"
                                      "border-radius: 10px;\n"
                                      "border-color: beige;\n"
                                      "background-color: rgb(185, 246, 255);\n"
                                      "")
        self.create_acc.setObjectName("create_acc")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "WELCOME TO PING"))
        self.label_2.setText(_translate("Dialog", "Sign in Or Create a New Account"))
        self.login.setText(_translate("Dialog", "Log In"))
        self.create_acc.setText(_translate("Dialog", "Create an Account"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
