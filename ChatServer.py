import socket
import sys
import threading


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
            try:
                client.send(message)
            except BrokenPipeError as e:
                if e.errno == 32:
                    print(addr, " --- > Connection lost")
                    connections.remove((client, addr))
                    continue
            print(message, len(connections))

    def recv_message(self, conn, addr):
        connected = True
        while connected:
            message = conn.recv(2048)
            if not message:
                sys.exit(0)
            connections = list(self.connections)
            connections.remove((conn, addr))
            self.send_message(message, connections)
        conn.close()

    def accept_connections(self):
        conn, addr = self.new_socket.accept()
        self.connections.append((conn, addr))
        return conn, addr

    def server_accept(self):
        while True:
            conn, addr = self.accept_connections()
            threading.Thread(target=self.recv_message, args=(conn, addr)).start()


if __name__ == '__main__':
    start_server = Server()
    start_server.server_accept()
