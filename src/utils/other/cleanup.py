# import libraries
import os, shutil

class Cleanup:
    @staticmethod
    def clean_directory(path_to_directory: str):
        # go through 'directory' files
        for filename in os.listdir(path_to_directory):
            # get the 'file' path
            file_path = os.path.join(path_to_directory, filename)

            # try to remove 'file/directory'
            try:
                # check if object is 'file/directory'
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    # unlink 'file'
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    # remove 'directory'
                    shutil.rmtree(file_path)
            except Exception as reason:
                # raise warning
                print('failed to delete %s. reason: %s' % (file_path, reason))

    @staticmethod
    def delete_directory(path_to_directory: str):
        # try to remove 'directory'
        try:
            # remove 'directory'
            os.rmdir(path_to_directory)
        except Exception as reason:
            # raise warning
            print('failed to delete %s. reason: %s' % (path_to_directory, reason))