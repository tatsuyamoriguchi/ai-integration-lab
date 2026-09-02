import json

application = {
    "company": "MSP A Co.",
    "role": "Sr. Solutions Engineer",
    "status": "Applied"
}

with open("application.json", "w") as file:
    json.dump(application, file, indent = 4)