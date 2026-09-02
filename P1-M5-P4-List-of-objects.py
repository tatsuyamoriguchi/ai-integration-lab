# 4. List of objects
# Create a list of 3 JobApplication instances. Loop through and print() each one 
# (relying on __str__).

class JobApplication:
    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status

    def __str__(self):
        return f"{self.company} - {self.role} - {self.status}"


applications = [
    JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied"),
    JobApplication("MSP B Co.", "Sales Engineer", "Recruiter's Screening"),
    JobApplication("MSP C Co.", "Implementation Engineer", "Interview 1")
]

for app in applications:
    print(app)

