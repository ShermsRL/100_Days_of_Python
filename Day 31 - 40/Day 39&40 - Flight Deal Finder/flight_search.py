import requests
from data_manager import DataManager

class FlightSearch(DataManager):
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        super().__init__()
        self.header = {
                "apikey": "mPtxMnpEU8s6qpWtVXVfS-CbmRWTHh1X",
            }

    def flight_search(self, city):
        url = "https://tequila-api.kiwi.com/locations/query"

        parameters = {
            "term": city,
            "location_types": "airport",

        }
        response = requests.get(url=url, params=parameters, headers=self.header)
        response_data = response.json()
        try:
            location_id = response_data['locations'][0]['id']
        except IndexError:
            return None
        else:
            return location_id




