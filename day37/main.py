import requests
import os
from datetime import date
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('PIXELA_USERNAME')
token = os.environ.get('PIXELA_API_KEY')

# Create user

pixela_api_url = "https://pixe.la/v1/users"

# params = {
#     'token' : token,
#     'username' : username,
#     'agreeTermsOfService' : 'yes',
#     'notMinor' : 'yes'
# }

# response = requests.post(url=pixela_api_url, json=params)

# Create a graph

# graph_url = f"{pixela_api_url}/{username}/graphs"

# params = {
#     'id' : 'walking',
#     'name' : 'Daily Steps',
#     'unit' : 'steps',
#     'type': 'int',
#     'color': 'shibafu',
#     'timezone': 'America/Toronto',
# }

# headers = {
#     'X-USER-TOKEN' : token
# }

# response = requests.post(url=graph_url, json=params, headers=headers)

# import ipdb; ipdb.set_trace()

# Create a Pixel

pixel_url = f"{pixela_api_url}/{username}/graphs/walking"

yesterday = date.today() - timedelta(days = 1)

steps = input("How many steps did you walk yesterday?")

params = {
    'date' : yesterday.strftime('%Y%m%d'),
    'quantity': steps
}

headers = {
    'X-USER-TOKEN' : token
}

response = requests.post(url=pixel_url, json=params, headers=headers)
print('Done')
# import ipdb; ipdb.set_trace()

# profile_url = f"https://pixe.la/@{username}"

# params = {
#     'pinnedGraphId': 'walking',
#     'timezone': 'America/Toronto'
# }

# headers = {
#     'X-USER-TOKEN' : token
# }

# response = requests.put(url=profile_url, json=params, headers=headers)
# import ipdb; ipdb.set_trace()

