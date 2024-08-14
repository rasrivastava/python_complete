"""
Client-side (start_client function):

The client creates a socket and connects to the server.
The client receives a message from the server and then closes the connection.
"""

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server address
host = socket.gethostname()  # Alternatively, use '127.0.0.1' for localhost
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Receive data from the server
message = client_socket.recv(1024)  # Buffer size is 1024 bytes
print(f"Message from server: {message.decode('ascii')}")

# Close the connection
client_socket.close()
