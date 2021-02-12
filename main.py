import requests
from datetime import datetime

# ----------------------------- ISS --------------------------

MY_LAT = 50.447731  # Kyiv
MY_LONG = 30.542721

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# ------------------------- TIME ---------------------------

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

time_now = datetime.now()
hour_now = time_now.hour


def is_iss():
    if MY_LAT - 5 < iss_latitude > MY_LAT + 5 and iss_longitude == MY_LONG:
        return True
    else:
        return False


def is_night():
    if sunrise < hour_now > sunset:
        return True
    else:
        return False


print(is_iss())
print(is_night())

if is_iss() and is_night():
    print('HEADS UP!')

# Your position is within +5 or -5 degrees of the ISS position.


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
