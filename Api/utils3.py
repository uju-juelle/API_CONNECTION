import requests

geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q=Lagos&limit=5&appid=4a1b20128003ece339da9d85069f32ce"

new = "http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=e872a9f3d44818ac5b5b5080b6cc9782"

response = requests.get(new)

print(response.json())