import requests
import json

api_key = 'Your_api_key'

source = input("From city: ")
destination = input("Destination city: ")

r = requests.get(f"https://maps.googleapis.com/maps/api/distancematrix/json?"
                 f"origins={source}"
                 f"&destinations={destination}"
                 f"&key={api_key}")
distance = r.json()
print(distance)
