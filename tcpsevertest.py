import socket
TCPserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 65520
ip_and_port = (ip, port)
TCPserver.bind(ip_and_port)
TCPserver.listen(5)
while True:
    connect,ip_and_port = TCPserver.accept()
    msg = 'Hello Client'.encode('utf-8')
    connect.send(msg)
    connect.close()