import socket


def client_1():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    message = "Привет, сервер!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()


def client_2():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    message = "Как дела?"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()


if __name__ == '__main__':
    client_1()
    print()
    client_2()
