import requests
import datetime
from flight_data import FLIGHT_DATA

TEQUILA_API_KEY = "J0EN4NyqqNwMJjUZHxZWWaSu17N3fkT9"
id = "sar13flightsearch"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
date = datetime.datetime.now().strftime("%d")
year = datetime.datetime.now().strftime("%Y")

class FLIGHT_SEARCH:
    def get_city_code(self,city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def flight_details(self,origin_city,destination,from_time,to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city,
            "fly_to": destination,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_info = FLIGHT_DATA(
            origin_city=data["route"][0]["cityFrom"],
            destination=data["route"][0]["cityTo"],
            to_date=data["route"][0]["local_departure"].split("T")[0],
            from_date=data["route"][1]["local_departure"].split("T")[0],
            price=data["price"],
        )
        print(f"{flight_info.destination}: {flight_info.price}")
        return flight_info