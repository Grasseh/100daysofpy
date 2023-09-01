import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response)
print(response.status_code)
data = response.json()['iss_position']
print(data)
print(data['longitude'])

my_lat = 45.851970
my_lon = -73.761000

params = {
    "lat": my_lat,
    "formatted": 0,
    "lon": my_lon
}

response = requests.get(url='http://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()
print(response.json())
