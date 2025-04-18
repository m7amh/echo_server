import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"[+] Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            command = data[0]
            string = data[1:]

            if command == 'A':
                result = ''.join(sorted(string, reverse=True))
            elif command == 'C':
                result = ''.join(sorted(string))
            elif command == 'D':
                result = string.upper()
            else:
                result = data

            conn.sendall(result.encode())
