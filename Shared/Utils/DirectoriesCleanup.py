import os
import shutil

class DirectoriesCleanup():
    def delete_content(path_to_directory: str):
        for filename in os.listdir(path_to_directory):

            file_path = os.path.join(path_to_directory, filename)

            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as reason:
                print('failed to delete %s. reason: %s' % (file_path, reason))

    def delete_directory(path_to_directory: str):
        try:
            os.rmdir(path_to_directory)
        except Exception as reason:
            print('failed to delete %s. reason: %s' % (path_to_directory, reason))