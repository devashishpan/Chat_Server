import os.path
import re
import socket
import sys
from datetime import datetime
from threading import *

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QFileDialog, QMessageBox
from PyQt5.uic import loadUi


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

    def send_message(self, message):
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
            return f'\n[{sender}]>> {message}'
        self.new_socket.close()

    def converse(self, server_ip):
        self.server_ip = server_ip
        self.connect_()


BUFFER_SIZE = 4 * 1024
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
s_ip = ""
start_client = Client()


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("server_login.ui", self)
        self.login.clicked.connect(self.goto_login)

    def goto_login(self):
        if re.search(regex, self.server_ip.text()):
            global s_ip
            s_ip = self.server_ip.text()
            try:
                #start_client.converse(s_ip)
                widget.addWidget(main_window)
                widget.setFixedHeight(450)
                widget.setFixedWidth(600)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            except Exception as e:
                self.error.setText(f"{e}Please Enter a valid IP....")
        else:
            self.error.setText("Please Enter a valid IP....")


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window.ui", self)
        self.file.clicked.connect(self.send_file)
        self.progressBar.setVisible(False)
        self.send.clicked.connect(self.send_messages)

    def send_file(self):
        path = QFileDialog.getOpenFileNames(self, 'Open a File', '', 'All Files (*.*)')
        filename = path[0][0]
        filesize = os.path.getsize(filename)
        total = round(filesize / BUFFER_SIZE) + 1
        completed = 0
        return
        if path != ([], ''):
            self.progressBar.setVisible(True)
            start_client.send_message(f"{filename}${filesize}".encode())
            self.send_files(f"{filename}")
            with open(filename, "rb") as f:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    print("File is empty!!")
                start_client.new_socket.sendall(bytes_read)
                completed += total / 100
                self.progressBar.setValue(completed)
        else:
            return 0
        self.send_completed()
        self.progressBar.setVisible(False)

    @staticmethod
    def send_completed():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("File Send Complete!!!!")
        msg.setWindowTitle("Information MessageBox")
        msg.setStandardButtons(QMessageBox.Ok)
        print(msg.exec_())

    def send_messages(self):
        message = self.message_box.text()
        if message != '':
            cursor = self.textArea.textCursor()
            if not cursor.atEnd():
                cursor.movePosition(QtGui.QTextCursor.End)
            formatted_datetime = datetime.now().strftime("%H:%M:%S")
            cursor.insertText(f'{formatted_datetime}:------------------\n{message}')
            cursor.insertBlock()
            # start_client.send_message(message)
        else:
            pass

    def received_message(self, message):
        if message != '':
            cursor = self.textArea.textCursor()
            if not cursor.atEnd():
                cursor.movePosition(QtGui.QTextCursor.End)
            formatted_datetime = datetime.now().strftime("%H:%M:%S")
            cursor.insertText(f'{formatted_datetime}:------------------\n{message}')
            cursor.insertBlock()
        else:
            pass

    def send_files(self, message):
        if message != '':
            cursor = self.textArea.textCursor()
            if not cursor.atEnd():
                cursor.movePosition(QtGui.QTextCursor.End)
            formatted_datetime = datetime.now().strftime("%H:%M:%S")
            cursor.insertText(f'{formatted_datetime}:------------------\n{message}')
            cursor.insertBlock()
        else:
            pass


app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("ping.jpeg"))
welcome = WelcomeScreen()
main_window = MainWindow()
widget = QStackedWidget()
widget.setWindowTitle("PING")
widget.addWidget(welcome)
widget.setFixedHeight(450)
widget.setFixedWidth(600)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting....")


class Recv(Thread):
    def run(self):
        message = start_client.recv_message()
        main_window.received_message(message)


if __name__ == '__main__':
    pass
    # Recv().start()
