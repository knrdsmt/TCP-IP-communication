# Socket File Transfer System

This repository contains two Python scripts for a simple client-server file transfer system using sockets.

## TCP/IP Protocol
- The communication between the server and clients is based on the TCP/IP protocol.
- TCP (Transmission Control Protocol) provides reliable, ordered, and error-checked delivery of data between applications.
- IP (Internet Protocol) handles the routing of data packets between devices on the network.

## Connecting and Communication

### Connection Establishment
- The server script (`server.py`) binds to a specific host and port using the `socket.bind()` method.
- It then listens for incoming connections using the `socket.listen()` method.
- When a client wants to connect, it creates a socket and uses the `socket.connect()` method to establish a connection to the server's host and port.

### Client-Server Interaction
- Once a connection is established, the client and server can communicate bidirectionally.
- The client sends messages or files to the server using the `socket.send()` method, specifying the data to send.
- The server receives data from clients using the `socket.recv()` method. It then processes the received data accordingly.
- In the case of file transfer, the client sends a specific command (`"SEND_FILE"`), followed by the filename, size, and file data. The server handles this special command to save the file.

### Threading for Concurrent Communication
- Both the client and server scripts use threading to handle multiple clients simultaneously.
- Each time a new client connects to the server, a new thread is created to handle communication with that client.
- This allows multiple clients to connect and interact with the server concurrently without blocking each other.

### Error Handling
- Both scripts implement error handling to ensure robustness and prevent unexpected crashes.
- Error handling includes catching exceptions such as socket errors or client disconnections.
- When errors occur, appropriate error messages are displayed, and the affected connections are gracefully closed.

### Running the System
1. Start the server script (`server.py`) first to listen for incoming connections.
2. Clients can then run the client script (`client.py`) to establish connections to the server.
3. Once connected, clients can send messages or files to the server, and the server can respond accordingly.

## Server Script

### Description
- **File:** `server.py`
- **Functionality:** This script sets up a server that listens for incoming connections from clients. It can handle multiple clients concurrently. When a client sends a file to the server, it saves the file in the server's directory.
- **Usage:** Run the script `server.py` to start the server.

### Usage
1. Run the server script `server.py`.
2. Connect clients to the server using the appropriate client script.
3. Clients can send files to the server by specifying the filename and size followed by the file data.

## Client Script

### Description
- **File:** `client.py`
- **Functionality:** This script sets up a client that can connect to a server. It allows users to send messages to the server. The client also receives messages from the server and displays them.
- **Usage:** Run the script `client.py` to start the client.

### Usage
1. Run the client script `client.py`.
2. Enter messages to send to the server.
3. The client displays messages received from the server.

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
