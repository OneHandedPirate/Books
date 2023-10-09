import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create tcp-server
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

connection, client_address = server_socket.accept()
print(f'Connection request from {client_address} received')
