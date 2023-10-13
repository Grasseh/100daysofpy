import requests
import os
from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv()

nutri_api_key = os.environ.get('NUTRITIONIX_API_KEY')
nutri_id_key = os.environ.get('NUTRITIONIX_ID_KEY')
exercise_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise = input("What exercise did you do?")

headers = {
    'x-app-key' : nutri_api_key,
    'x-app-id' : nutri_id_key
}

params = {
    "query" : exercise,
    "gender" : "male",
    "weight_kg" : 70.3,
    "height_cm" : 177.8,
    "age": 29
}

response = requests.post(url=exercise_url, json=params, headers=headers)
response_json = response.json()

calories = response_json['exercises'][0]['nf_calories']
exercise = response_json['exercises'][0]['name']
duration = response_json['exercises'][0]['duration_min']

headers = {
    'Authorization': 'Bearer rySCU6a^v,^rQ(=>c(4W'
}

params = {
    'workout' : {
        'date': datetime.now().strftime('%Y/%m/%d'),
        'time': datetime.now().strftime('%H:%M'),
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
}

sheet_url = 'https://api.sheety.co/9ae06ab60c6d6c3a5a2f54045fab564e/myWorkouts/workouts'

response = requests.post(url=sheet_url, json=params, headers=headers)
response_json = response.json()

# import ipdb; ipdb.set_trace()
