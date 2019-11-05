import socket
import select

def run():
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 8888        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.setblocking(False)
        line = ""
        while line != "quit":
            line = input(">> ")
            s.sendall(line.encode("ascii"))
            # the receive needs its own thread.

            try:
                # TODO figure out why this doesnt work.
                data = s.recv(500)
            except:
                data = ""
            print('Received', repr(data))


if __name__=="__main__":
    run()