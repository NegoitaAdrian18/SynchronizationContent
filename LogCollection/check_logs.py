import time


class LogMessage:

    @staticmethod
    def log(message):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('log_file.txt', 'a') as f:
            f.write('[' + now + ']' + message + '\n')
