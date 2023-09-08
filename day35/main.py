import requests

API_KEY = os.environ.get('API_KEy')
WEATHER_MAP_URL = 'https://api.openweathermap.org/data/2.5/weather'
ONE_CALL_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall'

MY_LAT = 45.851970
MY_LONG = -73.761000

params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY
}

response = requests.get(ONE_CALL_WEATHER_URL, params=params)
print(response.json())

# This endpoint is deprecated by OWM. This day will be skipped because of that
