# 1. Basic class
# Create a class JobApplication with __init__(self, company, role, status) storing all three 
# as attributes. Create two instances and print their .company and .status directly 
# (no methods yet).

class JobApplication:
    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status

applications = [
    JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied"),
    JobApplication("MSP B Co.", "Sales Engineer", "Recruiter's Screening")
]

for app in applications:
    print(f"{app.company} - {app.status}")