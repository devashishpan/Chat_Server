import socket
import threading
import time


class Server:
    def __init__(self, port=9999):
        self.new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.new_socket.bind(('', port))
        self.new_socket.listen(5)
        self.connections = []

    @staticmethod
    def send_message(message, connections):
        for (client, addr) in connections:
            client.send(message)

    def recv_message(self):
        for (client, addr) in self.connections:
            message = client.recv(2048)
            connections = list(self.connections)
            connections.remove((client, addr))
            self.send_message(message, connections)

    def accept_connections(self):
        self.connections.append(self.new_socket.accept())

    def server_accept(self):
        while True:
            accept_thread = threading.Thread(self.accept_connections())
            conv_thread = threading.Thread(self.recv_message())
            accept_thread.start()
            conv_thread.start()
