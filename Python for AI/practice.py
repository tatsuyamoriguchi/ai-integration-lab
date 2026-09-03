# 6. Combine everything (mini capstone) Build a simple tracker: a list of dictionaries, 
# each representing a job application (company, role, status). Loop through 
# and print a formatted status report for each one, using an f-string.

applications = [
    {
        "company": "MSP A Co",
        "role": "Sr. Solutions Architect",
        "status": "Applied"
    },
    {
        "company": "MSP B Co",
        "role": "Sr. Solutions Engineer",
        "status": "Rejected"
    },
    {
        "company": "MSP C Co",
        "role": "Sr. Sales Engineer",
        "status": "Hiring Manager Interview"
    }
]

for application in applications:
    print(f"company: {application["company"]}, role: {application["role"]}, status: {application["status"]}")
