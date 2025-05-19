from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel, QDesktopWidget
from PyQt5 import uic
from PyQt5 import QtCore
import sys
import requests
import time

class UI(QMainWindow):
    def __init__(self):  # Corrected method name
        super(UI, self).__init__()
        self.setObjectName("Form")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        uic.loadUi("btcp.ui", self)

        self.combo1 = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox, "comboBox_2")
        self.label = self.findChild(QLabel, "label")

        self.combo1.setEditable(True)
        self.combo1.setInsertPolicy(QComboBox.InsertAtTop)

        # Adding cryptocurrency options
        crypto_options = [
            "bitcoin", "ethereum", "tether", "binance-coin", "usd-coin", "cardano",
            "solana", "dogecoin", "polkadot", "shiba-inu", "polygon", "litecoin",
            "chainlink", "bitcoin-cash", "stellar", "uniswap", "avalanche",
            "cosmos", "wrapped-bitcoin", "algorand", "internet-computer", "vechain",
            "filecoin", "aave"
        ]
        self.combo1.addItems(crypto_options)

        # Adding time intervals
        time_intervals = ["now", "5 minutes", "15 minutes", "30 minutes",
                          "1 hour", "2 hours", "3 hours", "6 hours",
                          "12 hours", "day", "week", "month", "year"]
        self.combo2.addItems(time_intervals)

        self.combo1.activated.connect(self.clicker)
        self.combo2.activated.connect(self.clicker2)

        self.center()  # Center the window

        self.show()

    def center(self):
        # Center the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()  # Use QDesktopWidget here
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clicker(self):
        # Clear the second box (if needed)
        self.combo2.clear()
        # Add dependent items based on selection in combo1 (optional)
        time_intervals = ["now", "5 minutes", "15 minutes", "30 minutes",
                          "1 hour", "2 hours", "3 hours", "6 hours",
                          "12 hours", "day", "week", "month", "year"]
        self.combo2.addItems(time_intervals)

    def clicker2(self):
        crypto_id = self.combo1.currentText()
        time_label = self.combo2.currentText()

        # Mapping time labels to seconds
        time_mapping = {
            "now": 120, "5 minutes": 300, "15 minutes": 900,
            "30 minutes": 1800, "1 hour": 3600,
            "2 hours": 7200, "3 hours": 10800,
            "6 hours": 21600, "12 hours": 43200,
            "day": 86400, "week": 604800,
            "month": 2592000, "year" : 31536000
        }

        seconds_ago = time_mapping.get(time_label, 3600)  # Default to 1 hour if not found
        price = get_price_in_past(crypto_id, seconds_ago)

        if price is not None:
            self.label.setText(f'$ {price:.2f}')
        else:
            self.label.setText(f'No data available for {crypto_id} at {time_label}')

def get_price_in_past(crypto_id, seconds_ago):
    current_time = int(time.time())
    target_time = current_time - seconds_ago

    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart/range'
    params = {
        'vs_currency': 'usd',
        'from': target_time,
        'to': current_time }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for request errors
        data = response.json()

        if data['prices']:
            return data['prices'][-1][1]  # Last price
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":  # Corrected the module name check
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
