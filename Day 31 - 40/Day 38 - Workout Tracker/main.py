import requests
from datetime import datetime
import os
import pytz


HEADERS = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY"),
    "x-remote-user-id": "0",
    "Authorization": os.environ.get("TOKEN"),
}

parameters = {
    "query": input("What exercise did you do today?"),
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 175,
    "age": 24,

}

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutri_response = requests.post(url=natural_exercise_endpoint, json=parameters, headers=HEADERS)
print(nutri_response.text)
print(nutri_response.json()['exercises'][0]['name']) # activity
print(nutri_response.json()['exercises'][0]['duration_min']) # Duration
print(nutri_response.json()['exercises'][0]['nf_calories']) # Calories

timezone = pytz.timezone("Singapore")
today = datetime.now(timezone)
print(today)

num = 0
while num != len(nutri_response.json()['exercises']):
    sheety_endpoint = os.environ.get("SHEET_ENDPOINT")
    sheety_params = {
        "workout":{
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": (nutri_response.json()['exercises'][num]['name']).title(),
            "duration": nutri_response.json()['exercises'][num]['duration_min'],
            "calories": nutri_response.json()['exercises'][num]['nf_calories'],

        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=HEADERS)
    print(sheety_response.text)
    num += 1