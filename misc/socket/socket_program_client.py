import socket

# Create a socket object
client_socket = socket.socket()

# Define the server IP address and port
server_ip = '127.0.0.1'  # localhost (same machine)
server_port = 1234

# Connect to the server
client_socket.connect((server_ip, server_port))

# Receive data from the server
message = client_socket.recv(1024)  # Buffer size of 1024 bytes
print(f"Message from server: {message.decode()}")

# Close the connection
client_socket.close()
