import socket
import struct

# Server Configuration
HOST = '127.0.0.1'  # Listen on all interfaces
PORT = 12345      # Port to listen on

# Create and bind the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Allow only one connection

print(f"Server listening on {HOST}:{PORT}...")

# Accept the connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive 8 bytes of data
data = client_socket.recv(8)

# Unpack the 8 bytes into an integer
if len(data) == 8:
    unpacked_data = struct.unpack('!Q', data)  # '!Q' means big-endian, 8-byte unsigned integer
    print(f"Received integer: {unpacked_data[0]}")
else:
    print("Error: Expected 8 bytes, but received different amount.")

# Close the connection
client_socket.close()
server_socket.close()
