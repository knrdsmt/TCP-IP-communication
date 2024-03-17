import socket
import threading

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print("\nReceived message: ", message)
            else:
                break
        except:
            break

threading.Thread(target=receive_message).start()

try:
    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode())
except KeyboardInterrupt:
    print("Closing the client...")
    client_socket.close()
