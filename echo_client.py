import socket

def send_message(message, host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
        print("Server Response:", response)

if __name__ == "__main__":
    while True:
        msg = input("Enter command (A/C/D + string): ")
        if msg.lower() == "exit":
            break
        send_message(msg)
