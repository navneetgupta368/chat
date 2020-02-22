import socket

HOST = '216.58.203.196'
PORT = 80
server = (HOST,PORT)
request = '''GET / HTTP/1.0         
Host: www.google.org

'''

with socket.socket() as s:
    s.connect(server)
    s.sendall(request.encode())
    doc = ''
    while True:
        data = s.recv(1024)
        if not data:
            break
        doc += data.decode()
print(doc)