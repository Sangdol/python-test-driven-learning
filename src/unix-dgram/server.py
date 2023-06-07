import os
import socket

server_address = './uds_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# Bind the socket to the address
print('Starting up on {}'.format(server_address))
sock.bind(server_address)

while True:
    print('\nWaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('Received {} bytes from {}'.format(len(data), address))
    print(data)
