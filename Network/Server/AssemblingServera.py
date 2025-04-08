from ReceptionConection import Reception

class Assemmbling:
    def __init__(self, ip, port):
        self.connection = Reception(ip, port)
    def Start(self):
        sock, ip = self.connection.open_host()
        print(ip)