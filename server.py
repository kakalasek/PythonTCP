import socket


def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print(f'starting up on {server_address[0]} port {server_address[1]}')
    sock.bind(server_address)

    # Listen for incoming connection
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print('connection from ', client_address)

            # Recieve the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print(f'recieved "{data}"')
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no more data from ', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()


if __name__ == "__main__":
    main()