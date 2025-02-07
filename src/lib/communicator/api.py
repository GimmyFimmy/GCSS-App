import os.path

from src.lib.communicator.registry import Registry
from src.lib.communicator.communicator import Communicator

path_to_devices = os.path.abspath('devices')

class DevicesController:
    def __get_from_client(self, data, address):
        if not Registry.get_device(address):
            Registry.write_device(address, data)

        self.Communicator.send(address, 'ps')

    def __init__(self):
        self.Communicator = Communicator(self.__get_from_client)

    def start_listening(self):
        self.Communicator.start()

    def stop_listening(self):
        self.Communicator.stop()

    def get_devices(self):
        devices = []

        for device in os.listdir(path_to_devices):
            port = device[:4]

            devices.append(Registry.read_device(port))

        return devices

    def remove_device(self, port: str):
        Registry.remove_device(port)

    def set_gesture(self, port: str, key: str, value: str):
        device = path_to_devices + f'/{port}.txt'

        if os.path.exists(device):
            old_data = Registry.read_device(port)

            Registry.remove_device(port)

            new_file = open(device, 'w')

            for line in old_data:
                if list(line.split('='))[0] == key:
                    new_file.write(key + '=' + value + "\n")
                else:
                    new_file.write(line + "\n")

            new_file.close()

    def send_commands(self, gesture: str):
        devices = self.get_devices()

        for data in devices:
            keys = ""

            for line in data[3:]:
                key, value = line.split('=')

                if value == gesture:
                    keys += key + "_"

            if len(keys) != 0:
                address = (data[0], int(data[1]))

                self.Communicator.send(address, keys)