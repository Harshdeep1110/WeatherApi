import requests

api_key = "a987c05bba43ccf8797330cea3a7c6eb"
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name :")
request_url = f"{base_url}?appid={api_key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
