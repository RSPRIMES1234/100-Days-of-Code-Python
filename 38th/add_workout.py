import requests
from datetime import datetime


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
Application_ID="asdasdasd"
Application_Keys="asdasdasdasdasdasd"

url_excersise="	https://trackapi.nutritionix.com/v2/natural/exercise"


header_data={

    "x-app-id":Application_ID,
    "x-app-key":Application_Keys
}

excersise_params={
    "query":input("Tell me what excersise you did"),
}

response=requests.post(url=url_excersise,json=excersise_params,headers=header_data)
response.raise_for_status()
print(response.text)
response=response.json()
# duration=str(response[0]['duration_min'])
# calories=str(response[0]['nf_calories'])
# activity=response[0]['name'].title


url_sheety = 'https://api.sheety.co/fasdfddddddasdddddddddd/madasdad/dadasdasd'


for exercise in response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response=requests.post(url=url_sheety,json=sheet_inputs)
    print(response.text)