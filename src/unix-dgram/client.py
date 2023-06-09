import socket

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/uds_socket'
message = b'This is the message. It will be echoed.'

try:
    # Send data
    print('Sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

finally:
    print('Closing socket')
    sock.close()
