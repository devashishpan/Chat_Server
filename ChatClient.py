import socket
import threading


class Client:
    def __init__(self):
        self.new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)

    def connect_(self, server_ip, port=9999):
        self.new_socket.connect((server_ip, port))

    def check_connection(self, server_ip, port):
        try:
            self.connect_(server_ip, port)
            return True
        except OSError as e:
            if '101' in e:
                return False
            if '106' in e:
                return True
            else:
                print(e)
                return False

    def send_message(self):
        message = input('SEND>> ')
        self.new_socket.send(f'{self.host_ip}${message}'.encode())

    def recv_message(self):
        sender, message = tuple(self.new_socket.recv(2048).decode().split('$'))
        print(f'[{sender}]>> {message}')

    def converse(self, server_ip, port):
        self.connect_(server_ip, port)
        while self.check_connection(server_ip, port):
            send_thread = threading.Thread(self.send_message())
            send_thread.start()
            recv_thread = threading.Thread(self.recv_message())
            recv_thread.start()
            if self.close_connection():
                send_thread.join()
                recv_thread.join()
                self.new_socket.close()

    def close_connection(self):
        pass
