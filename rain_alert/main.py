import requests
from twilio.rest import Client

account_sid = "AC12710f06e476348b7a5fcfb51c1c652b"
try:
    auth_token = "9fae01a6273213c59156128c71c2de00"
except Exception as e:
    print("Auth not found")
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 37.76,
    "lon": 30.55,
    "appid": "92d27b43f4b0930b315744359bc669cb",
    "cnt": 5
}

response = requests.get(url=OWN_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["list"]
weather = []

for item in data:
    weather.append(item["weather"][0]["id"])

for item in weather:
    if item < 700:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="It's going to rain today Bring and umbrella ☂️.",
            from_='+12017629314',
            to='+14378557883'
        )
        print(message.status)
        break
