import socket

def main():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            send = input()
            s.sendall(send.encode('ascii'))
            data = s.recv(1024)
            print(f"Received {data!r}")


if __name__ == '__main__':
    main()