from Server import Server

server = Server("192.168.1.61", 4444)
client_socket, ip = server.listen_connection()
server.customer_data_processing(client_socket)
