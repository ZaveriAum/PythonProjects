import time
import requests
import datetime
import smtplib

MY_LAT = 43.751682
MY_LONG = -79.497788

MY_EMAIL = "zaveriaumhemang@gmail.com"
MY_PASSWORD = "zgbgkvrdqakfjjsj"


def is_iss_above_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    iss_longitude = float(response.json()['iss_position']['longitude'])
    iss_latitude = float(response.json()['iss_position']['latitude'])

    if 5 + MY_LAT >= iss_latitude >= MY_LAT - 5 and 5 + MY_LONG >= iss_longitude >= MY_LONG - 5:
        return True


parameter = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}


def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now()

    if sunrise > time_now.hour >= sunset:
        return True


while True:
    time.sleep(60)
    if is_iss_above_me() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject:International Space Station\n\nLook up.")
