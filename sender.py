import socket
import struct

# Server information
SERVER_IP = '127.0.0.1'  # IP of the server
PORT = 12345             # Port to connect to

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

# The integer to send
integer_to_send = 1234567890123456789  # Example large integer

# Pack the integer into 8 bytes (unsigned long long format)
packed_data = struct.pack('!Q', integer_to_send)  # '!Q' means big-endian, 8-byte unsigned integer

# Send the packed data
client_socket.sendall(packed_data)

# Close the connection
client_socket.close()
