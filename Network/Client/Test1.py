from Client import Client

client = Client("192.168.1.61", 4444)
sock = client.connect_to_server()
sock.send("HI".encode())
sock.recv(1024)