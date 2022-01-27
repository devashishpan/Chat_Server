import socket
import sys
from threading import *


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
start_client.converse(socket.gethostbyname(socket.gethostname()))


class Send(Thread):
    def run(self):
        while start_client.check_connection():
            start_client.send_message()


class Recv(Thread):
    def run(self):
        start_client.recv_message()


if __name__ == '__main__':
    Recv().start()
    Send().start()
