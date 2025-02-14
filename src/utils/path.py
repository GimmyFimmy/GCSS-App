import os

class Path:
    @staticmethod
    def exists(file: str):
        try:
            return (
                    os.path.isfile(file)
                    or os.path.islink(file)
                    or os.path.isdir(file)
                    )
        except OSError:
            print(f'[ERROR]: unable to check <{file}> existence!')

    @staticmethod
    def empty(directory: str):
        try:
            return len(os.listdir(directory)) == 0
        except OSError:
            print(f'[ERROR]: unable to check <{directory}> emptiness!')

    @staticmethod
    def get_parent_path():
        current_path = os.getcwd()

        return Path.get_path_to(os.path.join(current_path, os.pardir))

    @staticmethod
    def get_path_to(file: str, directory=None):
        assert(type(file) is str)

        try:
            if directory:
                return os.path.abspath(os.path.join(directory, file))
            else:
                return os.path.abspath(file)
        except OSError:
            print(f'[ERROR]: unable to get path to <{file}>!')

    @staticmethod
    def create_directory(directory: str):
        assert(type(directory) is str)

        try:
            os.makedirs(directory)
        except OSError:
            print(f'[ERROR]: unable to create <{directory}> directory!')

    @staticmethod
    def remove_file(file: str, directory=None):
        assert(type(file) is str)

        file_path = Path.get_path_to(file, directory)

        try:
            if Path.exists(file_path):
                os.unlink(file_path)
        except OSError:
            print(f'[ERROR]: unable to remove <{file}>!')

    @staticmethod
    def clean_directory(directory: str):
        assert(type(directory) is str)

        directory_path = Path.get_path_to(directory)

        for file in os.listdir(directory_path):
            Path.remove_file(file, directory_path)

    @staticmethod
    def remove_directory(directory: str):
        directory_path = Path.get_path_to(directory)

        try:
            if Path.exists(directory_path):
                Path.clean_directory(directory)

                if Path.empty(directory_path):
                    os.rmdir(directory_path)
                else:
                    print(f'[ERROR]: <{directory}> is not empty!')
        except OSError:
            print(f'[ERROR]: unable to remove <{directory}>!')