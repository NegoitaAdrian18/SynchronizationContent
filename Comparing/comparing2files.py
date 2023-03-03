import hashlib


class CompareFiles:

    @staticmethod
    def inspect_files(file1, file2):
        with open(file1, 'rb') as f1:
            with open(file2, 'rb') as f2:
                if hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest():
                    return True
                else:
                    return False
