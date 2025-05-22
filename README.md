# Crypto Price Viewer

A lightweight Python application with a PyQt5 GUI that displays historical cryptocurrency prices based on selected time intervals. The app fetches data from the CoinGecko API and presents it in a user-friendly interface.

## Features

- Choose from over 20 popular cryptocurrencies (e.g., Bitcoin, Ethereum, Dogecoin).
- Select time intervals such as "now", "5 minutes", "1 hour", "1 day", up to "1 year".
- Automatically fetches and displays the historical price in USD.
- Frameless and transparent GUI design.

## Previwe

- English
![1](https://github.com/user-attachments/assets/4f3b67e3-26c8-4fce-ae9d-3ad5cf27021f)


- Persian
![2](https://github.com/user-attachments/assets/884bf49c-26f9-4b00-b001-f27889313cc9)


## Prerequisites

- Python 3.x
- PyQt5
- `requests` library
- A UI file named `btcp.ui` in the same directory

## Installation

1. Clone the repository or copy the source files.
2. Make sure `btcp.ui` is present in the same directory as `btc.py`.
3. Install dependencies:

```bash
pip install PyQt5 requests
```

## Usage

Run the application with:

```bash
python btc.py
```

1. Select a cryptocurrency from the first dropdown.
2. Choose a time interval from the second dropdown.
3. The price will appear in the label area.

## API

This application uses the [CoinGecko API](https://www.coingecko.com/en/api) for retrieving cryptocurrency market data.

## Notes

- Make sure you have an active internet connection to fetch data.
- If no price data is available for a given time, a fallback message is shown.
