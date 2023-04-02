import requests
from twilio.rest import Client


api_key = ""
account_sid = ""
auth_token = ""

parameters = {
    'lat': 1.352083,
    'lon': 103.819839,
    'exclude': "current,minutely,daily",
    'appid': api_key,
}

code_list = []

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(response)
weather_data = response.json()
print(weather_data)

print(weather_data['hourly'][0]['weather'][0]['id']) # Get the weather code

for data in weather_data['hourly'][:12]:
    for code in data['weather']:
        code_list.append(code['id'])

print(code_list)

if any(num < 700 for num in code_list):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Its going to rain today, Bring umbrella!',
        from_='+18302712293',
        to='+6597622109'
    )
    print(message.status)