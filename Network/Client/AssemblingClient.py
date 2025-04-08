from ConectToServer import Connect

class Assembling:
    def __init__(self, ip_server, port_server):
        self.connect = Connect(ip_server, port_server)

    def Start(self):
        self.connect.connect_to_server()