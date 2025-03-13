import socket

def process_request(data):
    if not data:
        return ""

    command = data[0] 
    message = data[1:]

    if command == 'A':
        return ''.join(sorted(message)) 
    elif command == 'D':
        return ''.join(sorted(message, reverse=True)) 
    elif command == 'C':
        return message.upper()  
    else:
        return data  

def start_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f"Connected by {addr}")
                while True:
                    data = client_socket.recv(1024).decode().strip()
                    if not data:
                        break
                    response = process_request(data)
                    client_socket.sendall(response.encode())

if __name__ == "__main__":
    start_server()
