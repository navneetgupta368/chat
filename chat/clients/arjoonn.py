import socket


def connect(host, port=9999):
    server = (host, port)

    def send(msg):
        with socket.socket() as s:
            s.connect(server)
            s.sendall(msg.encode())

    def recv():
        with socket.socket() as s:
            s.connect(server)
            doc = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                doc += data
        return data

    return send, recv
