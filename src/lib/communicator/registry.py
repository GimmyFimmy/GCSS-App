import os.path

path_to_devices = os.path.abspath('devices')

class Registry:
    @staticmethod
    def write_device(address: tuple[str, int], data: list[str]):
        port = address[1]

        file = path_to_devices + f'/{port}.txt'

        if not os.path.exists(file):
            with open(file, 'w') as file:
                file.write(address[0] + "\n")
                file.write(str(address[1]) + "\n")
                file.write(data[0] + "\n")

                for value in data[1:]:
                    file.write(value + "=none\n")

                file.close()

    @staticmethod
    def read_device(port: str):
        assert(type(port) is str)

        file = path_to_devices + f'/{port}.txt'

        if os.path.exists(file):
            with open(file, 'r') as file:
                lines = [line.split('\n')[0] for line in file.readlines()]

            file.close()

            return lines

    @staticmethod
    def remove_device(port: str):
        assert(type(port) is str)

        file = path_to_devices + f'/{port}.txt'

        if os.path.exists(file):
            os.unlink(file)

    @staticmethod
    def get_device(address: tuple[str, int]):
        port = address[1]

        file = path_to_devices + f'/{port}.txt'

        return os.path.exists(file)