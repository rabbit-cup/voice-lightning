from Network.Client.StartClient import Client

client = Client("192.168.1.61", 4444)
print("Conect to server")
client.StartClient()