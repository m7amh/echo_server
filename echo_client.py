import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Type message starting with A/C/D or anything else to test:")
    while True:
        msg = input(">> ")
        if msg.lower() == 'exit':
            break
        s.sendall(msg.encode())
        data = s.recv(1024).decode()
        print("Server:", data)
