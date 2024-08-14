"""
Server-side (start_server function):

- A socket is created using socket.socket() with AF_INET (IPv4) and SOCK_STREAM (TCP).
- The server binds the socket to a host and port.
- The server listens for incoming connections.
- When a client connects, the server accepts the connection and sends a message.
"""

import socket

# Create a socket object
# The socket module provides access to the BSD socket interface, which is widely used for network communication.
# AF_INET: Address Family, indicating IPv4.
# `SOCK_STREAM: Socket type, indicating TCP (a reliable, connection-oriented protocol).
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Get the local machine name (or IP address)
host = socket.gethostname()  # Alternatively, use '127.0.0.1' for localhost
port = 12345

# Bind the socket to the port and IP
# The bind() method associates the socket with a specific IP address and port.
# Here, host is typically the server’s hostname or IP, and port is the port number where the server listens for connections.
server_socket.bind((host, port))

# Start listening for incoming connections
# The listen() method puts the server in listening mode.
# The parameter 1 specifies the number of unaccepted connections that the system will allow before refusing new connections.
server_socket.listen(1)

print("Server is listening...")

# Wait for a client to connect
# The accept() method blocks and waits for an incoming connection.
# Once a client connects, it returns a new socket object (client_socket) for the connection, and the client’s address (addr).
client_socket, addr = server_socket.accept()
print(f"Got a connection from {addr}")

# Send a message to the client
message = 'Hello, Client!'
# The server sends a message to the client using the send() method. The message is encoded as ASCII before sending.
client_socket.send(message.encode('ascii'))
# client_socket.send(message.encode())  # Send the string directly, defaults to UTF-8 encoding


# Close the connection
client_socket.close()
server_socket.close()
