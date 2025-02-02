import socket

LOCAL_PORT = 8888

BUFFER_SIZE = 1024

class Utils:
    @staticmethod
    def get_ip_address():
        temporary_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            temporary_socket.connect(("8.8.8.8", 80))

            return temporary_socket.getsockname()[0]
        finally:
            temporary_socket.close()

class Communicator:
    def __init__(self, listener):
        # check if 'function' type received
        assert(callable(listener))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        #self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.socket.bind(('', LOCAL_PORT))

        self.ip_address = Utils.get_ip_address()

        self._running = False

        self._callback = listener

    def start(self):
        assert(self._running is False)

        self._running = True

        while self._running:
            data, address = self.socket.recvfrom(1024)

            if data is not None:
                data = data.decode('utf-8').split('_')

                self._callback(data, address)

    def stop(self):
        assert(self._running is True)

        self._running = False

    def send(self, address: tuple[str, int], command: str):
        command = bytes(command, 'utf-8')

        self.socket.sendto(command, address)