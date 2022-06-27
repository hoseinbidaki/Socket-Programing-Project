import socket

HOST = '127.0.0.1' 
PORT = 65432    

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print('The server is running...')
server.listen()
while 1:
    conn, addr = server.accept()
    DECODE_TEXT = ''
    print('Connected with : ', addr)
    while True:
        data = conn.recv(1024)
        if not data : break
        DECODE_TEXT = data.decode('utf-8')
        if DECODE_TEXT == 'exit' : break
        print ('1 message received frrom ', PORT)
        data = bytes('server read it and change to : ' + DECODE_TEXT.upper(), 'utf-8')
        conn.sendall(data)
    
    conn.close()
    if DECODE_TEXT == 'exit' : break
server.close()
