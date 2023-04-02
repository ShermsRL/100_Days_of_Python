# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

price_dict = {}


data = DataManager()
sheet_data = data.read_sheet()
print(sheet_data)

search = FlightSearch()
flight_data_details = FlightData()
alert = NotificationManager()

for city in sheet_data:
    city['iataCode'] = search.flight_search(city['city'])
    data.write_sheet(city['id'], city['iataCode'])
    flight_price = flight_data_details.flight_data(city['city'], city['iataCode'])
    if flight_price[0] == city['city'] and flight_price[1] < city['lowestPrice']:
        alert.price_alert(price=flight_price[1],
                          from_city="Singapore",
                          from_city_code="SIN",
                          to_city=city['city'],
                          to_city_code=city['iataCode'],
                          from_date=flight_price[2],
                          to_date=flight_price[3],
        )
        alert.send_emails(flight_price[4],
                          price=flight_price[1],
                          from_city="Singapore",
                          from_city_code="SIN",
                          to_city=city['city'],
                          to_city_code=city['iataCode'],
                          from_date=flight_price[2],
                          to_date=flight_price[3])
    else:
        continue
