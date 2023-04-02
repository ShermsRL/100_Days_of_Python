import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header = {
            # Add in token here later for authorization to make it more secure
        }

        self.response = requests.get(url="https://api.sheety.co/a2569caa4695b9aab9211094f003dbd3/flightDeals/sheet1")

    def read_sheet(self):
        data = self.response.json()
        return data['sheet1']

    def write_sheet(self, id, code):
        edit_params = {
            "sheet1": {
                "iataCode": code
            }
        }
        edit_url = f"https://api.sheety.co/a2569caa4695b9aab9211094f003dbd3/flightDeals/sheet1/{id}"
        requests.put(url=edit_url, json=edit_params)


