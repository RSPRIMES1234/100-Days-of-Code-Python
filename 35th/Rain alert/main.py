import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient



proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = os.environ.get("acc_sid")
auth_token = os.environ.get("auth_token")




MY_LAT="00.677050"
MY_LONG="00.112091"
API_KEY=os.environ.get("api_token")

parameters={
"lat":MY_LAT,
"lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4

}



respon=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
respon.raise_for_status()
data=respon.json()
# print(data)
# print(data.keys())
weather1=data['list'][0]['weather'][0]['id']
weather2=data['list'][1]['weather'][0]['id']
weather3=data['list'][2]['weather'][0]['id']
weather4=data['list'][3]['weather'][0]['id']
# print(weather1)
# print(weather2)
# print(weather3)
# print(weather4)

if weather4 or weather2 or weather3 or weather1 <700:
    client = Client(account_sid, auth_token,http_client=proxy_client)

    message = client.messages.create(
        body="Bring a Umbrella",
        from_='+1811111111',
        to='+911111111111'
            )