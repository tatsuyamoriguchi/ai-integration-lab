import json

with open("applicaiton.json", "r") as file:
    data = json.load(file)

print(data["company"])
print(data["status"])