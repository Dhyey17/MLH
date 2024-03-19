from security import safe_requests

api_key = 'Your_api_key'

source = input("From city: ")
destination = input("Destination city: ")

r = safe_requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?"
                 f"origins={source}"
                 f"&destinations={destination}"
                 f"&key={api_key}", timeout=60)
distance = r.json()
print(distance)
