import requests
import pandas as pd

class CoinbaseAPI:
    def __init__(self, api_key, api_secret):
        self.base_url = "https://api.coinbase.com/v2/"
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {
            "CB-ACCESS-KEY": self.api_key,
            "CB-ACCESS-SIGN": self.api_secret,
            "CB-VERSION": "2022-11-15"  # API version
        }

    def get_cryptocurrency_data(self, currency_pair, start_date, end_date):
        endpoint = f"prices/{currency_pair}/historic?start={start_date}&end={end_date}"
        url = self.base_url + endpoint

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()['data']
            df = pd.DataFrame(data)
            return df
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

# Example usage:
api_key = "v7jFy9eiV2gsRqOs"
api_secret = "FG2gW7aODTVhcXYpeoZv3zkxBNRqWdKE"

coinbase = CoinbaseAPI(api_key, api_secret)
currency_pair = "BTC-USD"  # Example cryptocurrency pair
start_date = "2023-01-01"  # Start date for data retrieval
end_date = "2023-11-15"    # End date for data retrieval

crypto_data = coinbase.get_cryptocurrency_data(currency_pair, start_date, end_date)

if crypto_data is not None:
    print(crypto_data)

