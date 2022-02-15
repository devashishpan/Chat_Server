# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 450)
        self.audio_video = QtWidgets.QWidget(Dialog)
        self.audio_video.setGeometry(QtCore.QRect(0, 0, 371, 441))
        self.audio_video.setStyleSheet("border: 2px solid;\n"
"border-color: red;")
        self.audio_video.setObjectName("audio_video")
        self.audio = QtWidgets.QPushButton(self.audio_video)
        self.audio.setGeometry(QtCore.QRect(40, 400, 75, 23))
        self.audio.setObjectName("audio")
        self.video = QtWidgets.QPushButton(self.audio_video)
        self.video.setGeometry(QtCore.QRect(150, 400, 75, 23))
        self.video.setObjectName("video")
        self.stop = QtWidgets.QPushButton(self.audio_video)
        self.stop.setGeometry(QtCore.QRect(250, 400, 75, 23))
        self.stop.setObjectName("stop")
        self.vieo_screen = QtWidgets.QWidget(self.audio_video)
        self.vieo_screen.setGeometry(QtCore.QRect(10, 10, 351, 371))
        self.vieo_screen.setObjectName("vieo_screen")
        self.message_file = QtWidgets.QWidget(Dialog)
        self.message_file.setGeometry(QtCore.QRect(380, 0, 211, 441))
        self.message_file.setStyleSheet("border: 2px solid;\n"
"border-color: red;")
        self.message_file.setObjectName("message_file")
        self.messages = QtWidgets.QScrollArea(self.message_file)
        self.messages.setGeometry(QtCore.QRect(9, 9, 191, 341))
        self.messages.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.messages.setWidgetResizable(True)
        self.messages.setObjectName("messages")
        self.messaging_area = QtWidgets.QWidget()
        self.messaging_area.setGeometry(QtCore.QRect(0, 0, 187, 337))
        self.messaging_area.setObjectName("messaging_area")
        self.messages.setWidget(self.messaging_area)
        self.message_box = QtWidgets.QLineEdit(self.message_file)
        self.message_box.setGeometry(QtCore.QRect(10, 390, 141, 31))
        self.message_box.setText("")
        self.message_box.setObjectName("message_box")
        self.send = QtWidgets.QPushButton(self.message_file)
        self.send.setGeometry(QtCore.QRect(160, 389, 41, 31))
        self.send.setObjectName("send")
        self.file = QtWidgets.QPushButton(self.message_file)
        self.file.setGeometry(QtCore.QRect(10, 360, 75, 23))
        self.file.setObjectName("file")
        self.progressBar = QtWidgets.QProgressBar(self.message_file)
        self.progressBar.setGeometry(QtCore.QRect(90, 360, 111, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.audio.setText(_translate("Dialog", "Audio"))
        self.video.setText(_translate("Dialog", "Video"))
        self.stop.setText(_translate("Dialog", "STOP"))
        self.send.setText(_translate("Dialog", "Send"))
        self.file.setText(_translate("Dialog", "Send A file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

