import requests

Application_ID="asdasdasdaasdasdasdad"
Application_Keys="adasdasddasasdads"

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
response=response.json()["exercises"]
duration=response[0]['duration_min']
calories=response[0]['nf_calories']
activity=response[0]['name']