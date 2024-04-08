import socket
import subprocess as sb
import os

def date():
    return sb.check_output(["date"])

def help():
    return b'date\nhelp\nifconfig\nexit\n'

def ifconfig():
    return sb.check_output(["ifconfig"])


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
                match data:
                    case b'date':
                        conn.sendall(date())
                    case b'help':
                        conn.sendall(help())
                    case b'ifconfig':
                        conn.sendall(ifconfig())
                    case b'exit':
                        conn.sendall(b'break')
                        break
                    case _:
                        conn.sendall(b"Unknown command")



if __name__ == "__main__":
    main()

