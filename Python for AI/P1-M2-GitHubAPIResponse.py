import requests
import json

response = requests.get("https://api.github.com")

data = response.json() # Convert JSON obtained from GitHub to dict
print(json.dumps(data, indent=2))

