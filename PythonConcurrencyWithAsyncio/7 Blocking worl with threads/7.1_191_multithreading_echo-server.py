from threading import Thread
import socket


def echo(client: socket.socket):
    while True:
        data = client.recv(2048)
        print(f"Received data: {data}. Sending back...")
        client.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen()

    while True:
        client, client_address = (
            server_socket.accept()
        )  # блокируется в ожидании подключения юзера
        print(
            f"Connection request from {client_address} received"
        )  # при подключении юзера создается поток для выполнения функции echo

        thread = Thread(target=echo, args=(client,))

        thread.daemon = True
        thread.start()  # начало выполнения потока
