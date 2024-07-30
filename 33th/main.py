import time

import requests
import datetime as dt


MY_LAT=28.677050
MY_LONG=77.112091

def is_close():
    iss=requests.get(url="http://api.open-notify.org/iss-now.json")
    iss.raise_for_status()

    data=iss.json()
    iss_lat=float(data["iss_position"]["latitude"])
    iss_lang=float(data["iss_position"]["longitude"])
    if  (MY_LAT-5<=iss_lat<=MY_LAT+5) and (MY_LONG-5<=iss_lang<=MY_LONG+5) :
        return True
    return False


parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
    "tzid":"Asia/Calcutta"

}

now=dt.datetime.now()
response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset+sunset)
now_hour=now.hour






while True:
    while is_close():
        if now_hour>sunset or now_hour<sunrise:
            print("Look up")
        time.sleep(60)

    print("look down")
    time.sleep(60)