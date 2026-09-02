# 4. Logging basics
# Set up basic logging (logging.basicConfig(level=logging.INFO)), then log an INFO message 
# when your job application tracker script starts, and a WARNING message if any application 
# in your list has status == "Rejected".

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Job application tracker started")

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
    },
    {
        "company": "MSP X Co.",
        "role": "Solutions Architect",
        "status": "Rejected"
    }
]

for application in applications:
    if application["status"] == "Rejected":
        logging.warning(f"{application["company"]} rejected your application for {application["role"]}")
        
