# 5. DictionariesCreate a dictionary representing one job application:

# python
# application = {
#     "company": "Humina Resource",
#     "role": "Bilingual Sales Engineer",
#     "status": "submitted",
#     "follow_up_needed": True
# }
# Write code that checks follow_up_needed and prints a reminder message if True.

applications = [
    {
        "company": "Humina Resource",
        "role": "Biingual Sales Engineer",
        "status": "submitted",
        "follow_up_needed": True
    },
    {
        "company": "Trailor",
        "role": "Sr. Biingual Software Engineer",
        "status": "recruiter screen interview scheduled",
        "follow_up_needed": False
    },
    {
        "company": "Humina Resource",
        "role": "Biingual Sales Engineer",
        "status": "rejected",
        "follow_up_needed": False
    }
]

for application in applications:
    if application["follow_up_needed"]:
        print(f"Reminder: follow up with {application['company']} - status: {application["status"]}")