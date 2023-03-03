import os

from Comparing.comparing2files import CompareFiles


class CompareFolders:

    @staticmethod
    def inspect_folders(source_folder, backup_folder):
        source_files = os.listdir(source_folder)
        backup_files = os.listdir(backup_folder)

        if len(source_files) != len(backup_files):
            return False

        for file in source_files:
            if file in backup_files:
                if not CompareFiles.inspect_files(source_folder + '/' + file, backup_folder + '/' + file):
                    return False
            else:
                return False
        return True
