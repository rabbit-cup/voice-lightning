from AssemblingClient import Assembling

class Client:
    def __init__(self, ip_server, port_server):
        self.asm = Assembling("192.168.1.61", 4444)

    def StartClient(self):
        self.asm.Start()