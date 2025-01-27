import socket

from src.utils.logger import Logger

LOCAL_PORT = 8888

BUFFER_SIZE = 1024

Logger = Logger('communicator')

class Utils:
    @staticmethod
    def get_ip_address():
        temporary_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            temporary_socket.connect(("8.8.8.8", 80))

            return temporary_socket.getsockname()[0]
        except OSError:
            Logger.warning('failed to get <ip_address>')
        finally:
            temporary_socket.close()

class Communicator:
    def __init__(self, listener):
        # check if 'function' type received
        assert(callable(listener))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.socket.bind(('', LOCAL_PORT))

        self.id_address = Utils.get_ip_address()

        self._running = False
        self._callback = listener

        Logger.debug('initialized')

    def start(self):
        assert(self._running is False)

        self._running = True

        Logger.debug('listening began')

        while self._running:
            data, address = self.socket.recvfrom(1024)

            if data is not None:
                Logger.debug(f'received data from {address}')
                self._callback(data, address)

    def stop(self):
        assert(self._running is True)

        self._running = False

        Logger.debug('listening ended')

    def send(self, address, *args):
        Logger.debug(f'trying to send data to {address}')

        data = bytes(args)

        try:
            self.socket.sendto(data, address)
        except OSError:
            Logger.warning(f'failed to send data to {address}')