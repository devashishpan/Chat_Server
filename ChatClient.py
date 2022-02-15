import re
import socket
import sys
from threading import *

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget


class Client:
    def __init__(self):
        self.new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.server_ip = ""
        self.port = 9999

    def connect_(self, ):
        self.new_socket.connect((self.server_ip, self.port))

    def check_connection(self, ):
        try:
            self.connect_()
            return True
        except OSError as e:
            if e.errno == 101:
                return False
            if e.errno == 106:
                return True
            else:
                print(e)
                return False

    def send_message(self):
        message = input('SEND>> ')
        self.new_socket.send(f'{self.host_ip}${message}'.encode())

    def recv_message(self):
        while self.check_connection():
            recv_msg = self.new_socket.recv(2048)
            if not recv_msg:
                sys.exit(0)
            if not self.check_connection():
                self.new_socket.close()
                sys.exit(0)
            sender, message = tuple(recv_msg.decode().split('$'))
            print(f'\n[{sender}]>> {message}')
        self.new_socket.close()

    def converse(self, server_ip):
        self.server_ip = server_ip
        self.connect_()


start_client = Client()


class Send(Thread):
    def run(self):
        while start_client.check_connection():
            start_client.send_message()


class Recv(Thread):
    def run(self):
        start_client.recv_message()


class ServerLogin(QDialog):
    def __init__(self):
        super(ServerLogin, self).__init__()
        loadUi("server_login.ui", self)
        self.login.clicked.connect(self.goto_login)

    def goto_login(self):
        if re.search(regex, self.server_ip.text()):
            global s_ip
            s_ip = self.server_ip.text()
            try:
                start_client.converse(s_ip)
                self.close()
            except Exception as e:
                self.error.setText(f"{e}Please Enter a valid IP....")
        else:
            self.error.setText("Please Enter a valid IP....")


regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
s_ip = ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("ping.jpeg"))
    welcome = ServerLogin()
    welcome.setWindowTitle("PING")
    welcome.show()
    #Recv().start()
    #Send().start()
