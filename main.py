import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")

account_sid = "AC92a5533890a2caf5f02431e4d7c49b99"
auth_token = os.environ.get("AUTH_TOKEN")

q = {
    "lat": 33.748997,
    "lon": -84.387985,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=q)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_='+15076097388',
        to='+14703189931'
    )
    print(message.status)




