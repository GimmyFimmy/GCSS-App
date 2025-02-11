# import libraries
import socket

def get():
    # create 'socket: socket'
    temporary_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # connect to the 'socket: socket'
        temporary_socket.connect(("8.8.8.8", 80))

        # return 'ip_address: str'
        return temporary_socket.getsockname()[0]
    finally:
        # disconnect 'socket: socket'
        temporary_socket.close()