import socket


def main():

    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data == 'date':
                    conn.sendall(b'You called the date function!')
                else:
                    conn.sendall(b"Unknown command")



if __name__ == "__main__":
    main()