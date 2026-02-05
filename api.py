import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

data["current"]["temperature_2m"]


#Converting it into function
import requests

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"]

paris = get_weather(48.85, 2.35)
print(paris)

bangalore = get_weather(12.9629, 77.5775)
print(bangalore)

mysore = get_weather(12.2958, 76.6394)
print(mysore)