import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcome.ui", self)
        self.login.clicked.connect(self.goto_login)

    def goto_login(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.login_task)

    def login_task(self):
        user = self.username.text()
        passwd = self.password.text()

        if len(passwd) == 0 or len(user) == 0:
            self.error.setText("Please Fill All Fields....")
        else:
            if passwd == "12345":
                print("Logged In....")
                self.error.setText("")
            else:
                self.error.setText("Invalid User Name Or Password...")


app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("ping.jpeg"))
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.setWindowTitle("PING")
widget.addWidget(welcome)
widget.setFixedHeight(300)
widget.setFixedWidth(450)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting....")

if __name__ == "__main__":
    pass
