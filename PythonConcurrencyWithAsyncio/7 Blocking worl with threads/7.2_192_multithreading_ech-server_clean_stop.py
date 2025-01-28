from threading import Thread
import socket


class ClientEchoThread(Thread):
    def __init__(self, client: socket.socket):
        super().__init__()
        self.client = client

    def run(self):
        try:
            while True:
                data = self.client.recv(2048)
                if not data:
                    raise BrokenPipeError("Client disconnected")
                print(f"Received data: {data}. Sending back...")
                self.client.sendall(data)
        except OSError as e:
            print(f"Client disconnected: {e}. Shutting down")

    def close(self):
        if self.is_alive():
            self.client.sendall(bytes("Shutting down", encoding="utf-8"))
            self.client.shutdown(socket.SHUT_RDWR)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8000))
    server.listen()

    connection_threads = []

    try:
        while True:
            client, client_address = server.accept()
            print(f"Connection request from {client_address} received")
            thread = ClientEchoThread(client)
            thread.start()
            connection_threads.append(thread)
    except KeyboardInterrupt:
        print("Shutting down")
        for thread in connection_threads:
            thread.close()
