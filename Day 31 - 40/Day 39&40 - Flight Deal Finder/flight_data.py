import datetime
import requests
from datetime import *


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.departure_airport_code = "SIN"
        self.departure_city = "SIN"
        self.header = {
            "apikey": "mPtxMnpEU8s6qpWtVXVfS-CbmRWTHh1X",
        }
        self.date = datetime.now()

    def flight_data(self, city, id):
        url = "https://tequila-api.kiwi.com/v2/search"

        parameters = {
            "fly_from": self.departure_city,
            "fly_to": id,
            "date_from": self.date.strftime("%d/%m/%Y"),
            "date_to": (self.date + timedelta(days=180)).strftime("%d/%m/%Y"),
            "return_from": (self.date + timedelta(days=7)).strftime("%d/%m/%Y"),
            "return_to": (self.date + timedelta(days=28)).strftime("%d/%m/%Y"),
            "sort": "price",
            "curr": "SGD",
            "limit": 1,
            "max_stopover": 0,

        }

        response = requests.get(url=url, params=parameters, headers=self.header)
        response_data = response.json()
        nights_in_country = response_data['data'][0]['nightsInDest']
        arrival_date = (response_data['data'][0]['route'][0]['local_arrival']).split("T")
        arrival_date_obj = datetime.strptime(arrival_date[0], "%Y-%m-%d")
        return_date_obj = arrival_date_obj + timedelta(days=nights_in_country)
        print(response_data['data'][0]['deep_link'])
        return city, response_data['data'][0]['price'], arrival_date_obj.strftime("%d/%m/%Y"), return_date_obj.strftime("%d/%m/%Y"), response_data['data'][0]['deep_link']
