import socket

HOST = '127.0.0.1'  
PORT = 65432        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
while 1:
    msg = input()
    server.sendall(bytes(msg, 'utf-8'))
    data = server.recv(1024)
    print(data.decode('utf-8'))
    if (msg == 'exit') : 
        break
server.close()

