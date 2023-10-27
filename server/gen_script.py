# script for generating demo database

from hashlib import sha256
import random

logins = ['ivan', 'login', 'abcd', 'alex', 'andrey', 'petr', 'nick', 'oleg']
passwords = ['pass', '12345', 'qwerty', 'qwerty123', '123454321', 'zxcvbn', '2023', 'admin']

with open('db.txt', 'w') as file:
    for i in range(100):
        log = random.choice(logins)
        pas = random.choice(passwords)
        pas_hash = sha256(pas.encode('utf-8')).hexdigest() 
        file.write(f'{log}\t{pas}\t{pas_hash}\n')
