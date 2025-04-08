import socket

class Connect:
    def __init__(self, ip_server, port_server):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip_server
        self.port = port_server

    def connect_to_server(self):
        self.sock.connect((self.ip, self.port))