import sys
import json
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import pycurl
from ui_new_main import *

SERVER_URL = 'http://127.0.0.1:8000/api/v1/password_check'

def perform_request(login: str, password: str, accuracy: int) -> int:
    pass_hash = sha256(password.encode('utf-8')).hexdigest()
    hash_len = int((accuracy/100)*len(pass_hash))
    hash_to_send = pass_hash[:hash_len]

    headers = [
        'accept: application/json',
        'Content-Type: application/json',
    ]
    data = {
        'login': login,
        'password_hash': hash_to_send
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
        self.initial_accuracy = 25
        self.middle_accuracy = 50
        self.max_accuracy = 100

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widgets = self.ui

        self.widgets.stackedWidget.setCurrentWidget(self.widgets.home)

        self.show()
        self.setFixedSize(300, 360)
        self.widgets.pushButtonCheck.clicked.connect(self.perform_check)
        self.widgets.pushButton_2.clicked.connect(self.second_check)
        self.widgets.pushButton_4.clicked.connect(self.final_check)
        self.widgets.pushButton_5.clicked.connect(sys.exit)
        self.widgets.pushButton_3.clicked.connect(sys.exit)

    def second_check(self):
        accuracy = self.middle_accuracy if self.widgets.radioButton.isChecked() else self.max_accuracy
        result = perform_request(self.login, self.password, accuracy)
        if result == 0:
            QMessageBox.information(self, 'Success', 'Credentials are secure')
            return
        else:
            if accuracy == self.max_accuracy:
                if result == 1:
                    QMessageBox.warning(self, 'Warning', 'Password is compromised!')
                else:
                    QMessageBox.critical(self, 'Danger', 'Credentials pair is compromised!')
                self.widgets.stackedWidget.setCurrentWidget(self.widgets.home)
            else:
                self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_3)

    def final_check(self):
        result = perform_request(self.login, self.password, self.max_accuracy)
        if result == 0:
            QMessageBox.information(self, 'Success', 'Credentials are secure')
        elif result == 1:
            QMessageBox.warning(self, 'Warning', 'Password is compromised!')
        else:
            QMessageBox.critical(self, 'Danger', 'Credentials pair is compromised!')
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.home)

    def perform_check(self):
        self.login = self.widgets.lineEditLogin.text()
        if not self.widgets.lineEditPass.text():
            QMessageBox.critical(self, 'Error', "Password field can't be empty")
            return

        self.password = self.widgets.lineEditPass.text()
        try:
            result = perform_request(self.login, self.password, self.initial_accuracy)
        except ConnectionError as err:
            QMessageBox.critical(self, 'Error', str(err))
            return

        if result == 0:
            QMessageBox.information(self, 'Success', 'Credentials are secure')
            return

        self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
