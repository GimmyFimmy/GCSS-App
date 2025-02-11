"""
    NAME: communicator.py

    DESC: solution for sending and receiving data using Wi-Fi

    PRIVATE METHODS:
        __init__ -> initializes util

    PUBLIC METHODS:
        start -> starts listening and callbacks data, address
        stop -> stops listening
        send -> sends data to address
"""

# import libraries
import socket

from src.utils import byte

from src.constants import LOCAL_PORT
from src.constants import BUFFER_SIZE

class Communicator:
    def __init__(self, listener):
        # check if 'function' type received
        assert(callable(listener))

        # create 'socket: socket'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # configure 'socket: socket'
        #self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # bind local address to 'socket: socket'
        self.socket.bind(('', LOCAL_PORT))

        # create variables
        self._running = False
        self._callback = listener

    def start(self):
        # check if not 'running'
        assert(self._running is False)

        # set 'running: bool' as True
        self._running = True

        print('start listening!')

        # update 'listener: function'
        while self._running:
            # receive 'data: bytes' and 'address: tuple'
            data, address = self.socket.recvfrom(BUFFER_SIZE)

            print('received data!')

            # check if 'data: bytes' received
            if data is not None:
                # encode 'data: bytes'
                data = byte.decode(data)

                # callback 'data: str' and 'address: tuple'
                self._callback(data, address)

    def stop(self):
        # check if 'running'
        assert(self._running is True)

        # set 'running: bool' as False
        self._running = False

    def send(self, address: tuple[str, int], command: str):
        # encode 'command: str'
        command = bytes(command, 'utf-8')

        # send 'command: str' to 'address: tuple'
        self.socket.sendto(command, address)