import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create tcp-server
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()

connections = []

try:
    while True:
        connection, client_address = server_socket.accept()
        print(f"Connection request from {client_address} received")
        connections.append(connection)

        for connection in connections:
            buffer = b""

            while buffer[-2:] != b"\r\n":
                data = connection.recv(2)

                if not data:
                    break
                else:
                    print(f"Received data: {data}")
                    buffer += data

            print(f"All received data: {buffer}")

            connection.send(buffer)
finally:
    server_socket.close()
