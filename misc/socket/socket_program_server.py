import socket

# Create a socket object
s = socket.socket()

# Specify IP address and port number
ip = ""  # Empty string means bind to all interfaces
port = 1234

# Bind the socket to the IP address and port
s.bind((ip, port))
print(f"Server listening on port {port}...")

# Listen for incoming connections
s.listen()

# Accept an incoming connection
csession, addr = s.accept()

# Print the client's address
print(f"Connected to {addr}")

# Example: Send a welcome message to the client
welcome_message = "Welcome to the server!"
csession.send(welcome_message.encode())

# Close the client session and server socket
csession.close()
s.close()
