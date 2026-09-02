# 2. Add a method
# Add a method mark_rejected(self) that sets self.status = "Rejected". Test it 
# by creating an instance, printing its status, calling mark_rejected(), 
# then printing status again to confirm it changed.

class JobApplication:
    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status

    def mark_rejected(self):
        self.status = "Rejected"


applications = [
    JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied"),
    JobApplication("MSP B Co.", "Sales Engineer", "Recruiter's Screening")

]

for app in applications:
    print(f"{app.company} - {app.role} - {app.status}")
    if app.company == "MSP B Co.":
        app.mark_rejected()
        print("-- Status Updated --")
        print(f"{app.company} - {app.role} - {app.status}")    
