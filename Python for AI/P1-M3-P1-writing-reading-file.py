# 1. Write and read a text file
# Create a file job_search_log.txt. Write 3 lines to it (one per line) logging today's activity 
# (e.g., "Applied to MSP A Co."). Then read the file back and print its contents.

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
with open("job_search_log.txt", "w") as file:
    json.dump(applications, file, indent=4)

with open("job_search_log.txt", "r") as file:
    data = json.load(file)

for job in data:
    print(job["company"])
    print(job["role"])
    print(job["status"])
