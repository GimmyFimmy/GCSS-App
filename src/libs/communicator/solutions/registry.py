"""
    NAME: registry.py

    DESC: solution for adding, removing, rewriting devices data

    STATIC METHODS:
        write_device -> saves device id_address, port, name, functions in file
        rewrite -> changes specific device data in file
        read_device -> returns device id_address, port, name, functions
        remove_device -> removes device file
        get_device -> returns file existence
"""
import os

# import libraries
from src.constants import Path
from src.constants import DEVICES_PATH

class Registry:
    @staticmethod
    def write_device(address: tuple[str, int], data: list[str]):
        # get 'port: int'
        port = address[1]

        # get 'file'
        file = DEVICES_PATH + f'/{port}.txt'

        # check if 'file' exists
        if not Path.exists(file):
            # create new 'file'
            with open(file, 'w') as file:
                # write 'ip_address: str'
                file.write(address[0] + "\n")
                # write 'port: int'
                file.write(str(address[1]) + "\n")
                # write 'name: str'
                file.write(data[0] + "\n")

                # get through device functions
                for value in data[1:]:
                    # write device 'function: str'
                    file.write(value + "=none\n")

                # save new 'file'
                file.close()

    @staticmethod
    def rewrite_device(port: str, key: str, value: str):
        # check if 'str' type received
        assert(type(port) is str)
        # check if 'str' type received
        assert(type(key) is str)
        # check if 'str' type received
        assert(type(value) is str)

        # get 'file'
        file = DEVICES_PATH + f'/{port}.txt'

        # check if 'file' exists
        if Path.exists(file):
            # read 'file' data
            old_data = Registry.read_device(port)

            # remove 'file'
            Registry.remove_device(port)

            # create new 'file'
            new_file = open(file, 'w')

            # get through old data
            for line in old_data:
                # check if 'key: str' exists
                if list(line.split('='))[0] == key:
                    # write new 'value: str' to 'key: str'
                    new_file.write(key + '=' + value + "\n")
                else:
                    # write old 'line: str'
                    new_file.write(line + "\n")

            # save new 'file'
            new_file.close()

    @staticmethod
    def read_device(port: str):
        # check if 'str' type received
        assert(type(port) is str)

        # get 'file'
        file = DEVICES_PATH + f'/{port}.txt'

        # check if 'file' exists
        if Path.exists(file):
            # open 'file'
            with open(file, 'r') as file:
                # read 'line: str'
                lines = [line.split('\n')[0] for line in file.readlines()]

            # close 'file'
            file.close()

            # return 'lines: array'
            return lines

    @staticmethod
    def remove_device(port: str):
        # check if 'str' type received
        assert(type(port) is str)

        # get 'file'
        file = DEVICES_PATH + f'/{port}.txt'

        # remove 'file'
        Path.remove_file(file)

    @staticmethod
    def get_device(address: tuple[str, int]):
        # get 'port: int'
        port = address[1]

        # get 'file'
        file = DEVICES_PATH + f'/{port}.txt'

        # return bool
        return Path.exists(file)

    @staticmethod
    def get_devices():
        if Path.empty(DEVICES_PATH):
            print('[WARNING]: devices directory is empty')
            return

        devices_data = []

        for device in os.listdir(DEVICES_PATH):
            port, file_format = device.split('.')

            data = Registry.read_device(port)

            devices_data.append(data)

        return devices_data