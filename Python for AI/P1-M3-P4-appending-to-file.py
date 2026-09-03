import json

with open("applications.json", "r") as file:
    applications = json.load(file)




new_application = {
    "company": "MSP X Co.",
    "role": "Solutions Architect",
    "status": "Rejected"
}

applications.append(new_application)
with open("applications.json","w") as file:
    json.dump(applications, file, indent=4)


with open("applications.json", "r") as file:
    data = json.load(file)

for application in data:
    print(application["company"])
    print(application["role"])
    print(application["status"])