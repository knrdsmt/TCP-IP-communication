import socket
import threading
import os

HOST = 'localhost'
PORT = 12345

clients = []

mutex = threading.Lock()

def client_handler(client_socket):
    with mutex:
        clients.append(client_socket)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            if data.decode() == "SEND_FILE":
                file_name = client_socket.recv(1024).decode()
                file_size = int(client_socket.recv(1024).decode())
                with open(file_name, 'wb') as file:
                    received_data = 0
                    while received_data < file_size:
                        fragment = client_socket.recv(1024)
                        file.write(fragment)
                        received_data += len(fragment)
                print(f"Received file: {file_name}")
            else:
                with mutex:
                    for other_client in clients:
                        if other_client != client_socket:
                            other_client.send(data)
        except Exception as e:
            print(f"Error: {e}")
            break
    with mutex:
        clients.remove(client_socket)
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}")

try:
    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address}")
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()
except KeyboardInterrupt:
    print("Closing the server...")
    server_socket.close()
    for client in clients:
        client.close()
