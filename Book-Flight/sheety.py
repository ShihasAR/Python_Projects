import requests



url = "https://api.sheety.co/d8de9a9beb00fa84688893ba1c362b2a/copyOfFlightDeals/prices"
put_url = "https://api.sheety.co/d8de9a9beb00fa84688893ba1c362b2a/copyOfFlightDeals/prices"
                                      #SHEETY


SHEETY_PRICES_ENDPOINT = url

class SHEETY:
    def __init__(self):
        self.destination_data = {}

    def dest_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["price"]
        return self.destination_data