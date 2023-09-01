import requests
from datetime import datetime, timezone

MY_LAT = 45.851970 # Your latitude
MY_LONG = -73.761000 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def is_close_enough(my_lat, my_lon, iss_lat, iss_lon):
    lat_difference = abs(my_lat - iss_lat)
    lon_difference = abs(my_lon - iss_lon)
    return lat_difference <= 5 and lon_difference <= 5

def is_dark(sunrise, sunset, current_hour):
    return sunrise >= current_hour or sunset <= current_hour

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# import ipdb; ipdb.set_trace()
if (
    is_dark(sunrise, sunset, time_now.hour) and
    is_close_enough(MY_LAT, MY_LONG, iss_latitude, iss_longitude)
):
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    sender = "Stevo <steve@grasseh.com>"
    receiver = f"Stevo <steve@grasseh.com>"

    message = f"""\
Subject: LOOK UP
To: {receiver}
From: {sender}

{content}"""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        print(server.login(username, password))
        print(server.sendmail(sender, receiver, message))

