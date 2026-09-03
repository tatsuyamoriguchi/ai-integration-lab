import json

applications = [
    {
        "company": "MSP A Co.",
        "role": "Sr. Solutions Engineer",
        "status": "Applied"
    },
    {
        "company": "MSP B Co.",
        "role": "Sales Engineer",
        "status": "Recruiter's Screening"
    }

]

with open ("applications.json", "w") as file:
    json.dump(applications, file, indent=4)