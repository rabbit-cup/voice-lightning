import logging
import socket


class Server:
    def __init__(self, ip_server, port_server):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self._sock.bind((ip_server, port_server))
        except TypeError:
            logging.warning(f"TypeError Desc: IP = str and port = int")
        except socket.gaierror:
            logging.warning(f"socket.gaierror: Не коректный адрес")
        except OSError:
            logging.warning("OSError: Требуемый адрес для своего контекста неверен")

        self._sock.listen(10)

    def listen_connection(self):
        return self._sock.accept()

    @staticmethod
    def customer_data_processing(client_socket):
        while True:
            data = client_socket.recv(1024).decode()
            print(data)
