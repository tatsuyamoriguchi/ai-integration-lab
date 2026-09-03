# 3. Add __str__
# Add a __str__(self) method that returns a formatted one-line summary. 
# Create an instance and just print(instance) directly — no need to call any method.

class JobApplication:
    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status

    def __str__(self):
        return f"{self.company} - {self.role} - {self.status}"


applications = [
    JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied"),
    JobApplication("MSP B Co.", "Sales Engineer", "Recruiter's Screening")

]

for app in applications:
    print(app) # Calling the instance, app, automatically executes def __str__(self)

# The mental model
# Think of __str__ as plugging into a socket that Python already knows how to use 
# — you write the method, but you never call it yourself. It's similar in spirit 
# to conforming to CustomStringConvertible in Swift and implementing var description: 
# String — you define it once, and then print() (or string interpolation) automatically 
# knows to use it.