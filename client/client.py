import sys
import json
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import pycurl
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

SERVER_URL = 'http://127.0.0.1:8000/api/v1/password_check'

def perform_request(login: str, password: str) -> int:
    pass_hash = sha256(password.encode('utf-8')).hexdigest()
    headers = [
        'accept: application/json',
        'Content-Type: application/json',
    ]
    data = {
        'login': login,
        'password_hash': pass_hash
    }
    data_json = json.dumps(data)

    curl = pycurl.Curl()
    buffer = BytesIO()
    curl.setopt(pycurl.URL, SERVER_URL)
    curl.setopt(pycurl.HTTPHEADER, headers)
    curl.setopt(pycurl.POST, 1)
    curl.setopt(pycurl.POSTFIELDS, data_json)
    curl.setopt(pycurl.WRITEDATA, buffer)
    try:
        curl.perform()
    except pycurl.error as err:
        raise ConnectionError(str(err))

    response_code = curl.getinfo(pycurl.RESPONSE_CODE)
    curl.close()
    if not response_code == 200:
        raise ConnectionError(f'Connection error code: {response_code}')
    body = json.loads(buffer.getvalue().decode())
    return body['result']


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(str(Path(__file__).parent.resolve()) + '/main.ui', self)
        self.setWindowTitle("Credentials checker")
        self.setWindowIcon(QIcon("key.ico"))
        self.setFixedSize(300, 360)
        self.pushButton.clicked.connect(self.perform_check)
        
    def perform_check(self):
        login = self.lineEditLogin.text()
        if not self.lineEditPass.text():
            QMessageBox.critical(self, 'Error', "Password field can't be empty")
            return

        password = self.lineEditPass.text()
        try:
            result = perform_request(login, password)
        except ConnectionError as err:
            QMessageBox.critical(self, 'Error', str(err))
            return

        if result == 0:
            QMessageBox.information(self, 'Success', 'Credentials are secure')
        elif result == 1:
            QMessageBox.warning(self, 'Warning', 'Password is compromised!')
        else:
            QMessageBox.critical(self, 'Danger', 'Credentials pair is compromised!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
