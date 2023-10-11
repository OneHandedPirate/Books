import selectors
import socket
from selectors import SelectorKey


selector = selectors.DefaultSelector()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create tcp-server
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)  # Set server socket blocking flag to False

selector.register(server_socket, selectors.EVENT_READ)


while True:
    events: list[tuple[SelectorKey, int]] = selector.select(timeout=1)  # set selector timeout

    if len(events) == 0:   # check for events every timeout seconds
        print('Waiting for events...')

    for event, _ in events:
        event_socket = event.fileobj  # get event target socket

        if event_socket == server_socket:  # if event target socket is server_socket then event is connection attempt
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'Connection request from {address} received')
            selector.register(connection, selectors.EVENT_READ)  # register new client socket in selector
        else:
            data = event_socket.recv(1024)  # if event target socket is client socket - get data from it and send it back
            print(f'Received data: {data} from {event_socket}')
            event_socket.send(data)
