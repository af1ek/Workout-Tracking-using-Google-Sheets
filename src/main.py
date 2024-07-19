import requests
from datetime import datetime
import os


API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]

GENDER = "male"
WEIGHT_KG = 63
HEIGHT_CM = 175
AGE = 20

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")


headers = {"x-app-id": APP_ID,
           "x-app-key": API_KEY,
           "x-remote-user-id": "0"}

sheety_header = {"Authorization": SHEETY_AUTH}

exercise_text = input("Tell me which exercises you did: ")


parametri = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE}

response = requests.post(url=nutritionix_endpoint, headers=headers, json=parametri)
data = response.json()

sheety_input = {}
for exercise in data["exercises"]:
    sheety_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
}
    response_sheety = requests.post(url=sheety_endpoint, json=sheety_input, headers=sheety_header)
    print(response_sheety.text)
