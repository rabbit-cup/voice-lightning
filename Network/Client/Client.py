import logging
import socket


class Client:
    def __init__(self, ip_server, port_server):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._ip = ip_server
        self._port = port_server

    def connect_to_server(self):
        try:
            self._sock.connect((self._ip, self._port))
            return self._sock
        except TypeError:
            logging.warning("TypeError: ip = str and port == int")
        except socket.gaierror:
            logging.warning("socket.gaierror: Некоректный адрес")
        except ConnectionRefusedError:
            logging.warning("ConnectionRefusedError [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение")

