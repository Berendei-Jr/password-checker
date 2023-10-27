import os
from hashlib import sha256
from pathlib import Path

DB_FILE = str(Path(__file__).parent.resolve()) + '/db.txt'

class PasswordChecker:

    @staticmethod
    def init():
        if not os.path.exists(DB_FILE):
            raise FileNotFoundError('db file is not found')

    @staticmethod
    def check_credentials(login: str, pass_hash: str) -> int:
        with open(DB_FILE, 'r') as file:
            pass_found = False

            for line in file:
                words = line.split()
                if words[2] == pass_hash:
                    pass_found = True
                    if words[0] == login:
                        return 2

            return int(pass_found)    

    @staticmethod
    def add_password(password: str) -> None:
        pass_hash = sha256(password.encode('utf-8')).hexdigest()
        if PasswordChecker.check_password(pass_hash):
            return
        with open(DB_FILE, 'a') as file:
            file.write(f'{password}\t{pass_hash}\n')
