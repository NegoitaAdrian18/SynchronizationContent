import os
import time
from Comparing.comparing2files import CompareFiles
from Comparing.comparing2folders import CompareFolders
from LogCollection.check_logs import LogMessage


class Checking:

    def __init__(self):
        self.main_folder = str(input("Insert the path to the main folder:"))
        self.backup_folder = str(input("Insert the path to the backup folder:"))
        self.synchronization_interval = int(input("Insert the synchronization interval:"))

    def check_folder_presence(self):
        if not os.path.isdir(self.main_folder):
            LogMessage.log('main folder DOES NOT EXIST!')
            print('main folder DOES NOT EXIST!')
            exit()

    def check_backup_presence(self):
        if not os.path.isdir(self.backup_folder):
            LogMessage.log('backup folder DOES NOT EXIST!')
            print('backup folder DOES NOT EXIST!')
            exit()

    def check_folder_backup_the_same(self):
        while True:
            if CompareFolders.inspect_folders(self.main_folder, self.backup_folder):
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f'[{now}] Files are synchronized!')
                LogMessage.log('Files are synchronized!')
                time.sleep(self.synchronization_interval)
                continue

            if os.path.isdir(self.main_folder):
                print('main folder it is PRESENT!')
                LogMessage.log('main folder it is PRESENT!')
            else:
                print('main folder is not present')
                LogMessage.log('main folder is not present')
                break

            if os.path.isdir(self.backup_folder):
                print('backup folder it is PRESENT!')
                LogMessage.log('backup folder it is PRESENT!')
            else:
                print('backup folder is not present')
                LogMessage.log('backup folder is not present')
                break

            count_synchronization = 0
            update_file = 0
            delete_file = 0

            files = os.listdir(self.main_folder)
            files_backup = os.listdir(self.backup_folder)

            for file in files_backup:
                if file in files:
                    if CompareFiles.inspect_files(self.main_folder + '/' + file, self.backup_folder + '/' + file):
                        LogMessage.log(f'{file} is synchronized!')
                        count_synchronization += 1
                    else:
                        update_file += 1
                        os.remove(self.backup_folder + '/' + file)
                        os.system('cp -r ' + self.main_folder + '/' + file + ' ' + self.backup_folder)
                        LogMessage.log(f'{file} is updated')
                if file not in files:
                    LogMessage.log(f'{file} is deleted')
                    delete_file += 1
                    os.remove(self.backup_folder + '/' + file)

            for file in files:
                if file not in files_backup:
                    update_file += 1
                    LogMessage.log(f'{file} is copied')
                    os.system('cp -r ' + self.main_folder + '/' + file + ' ' + self.backup_folder)

            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f'[{now}] files synchronized: {count_synchronization}; files updated: {update_file}; files deleted: {delete_file};')

            time.sleep(self.synchronization_interval)
