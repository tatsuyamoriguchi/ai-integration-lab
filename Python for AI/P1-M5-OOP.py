# Defining a Class
# class JobApplication:
#     def __init__(self, company, role, status):
#         self.company = company
#         self.role = role
#         self.status

# Compare to Swift
# class JobApplication {
#     var company: String
#     var role: String
#     var status: String

#     init(company: String, role: String, status: String) {
#         self.company = company
#         self.role = role
#         self.status = status
#     }
# }

# Nearly identical shape. Key differences:
# __init__ is Python's initializer (double underscores — pronounced "dunder init", 
# short for "double underscore init")
# No type declarations required — Python doesn't force you to write company: String, 
# though you can add type hints (we'll touch this later)
# self must be the first parameter of every method, explicitly written — Swift hides this 
# from you, Python makes it visible



# Creating an Instance 
# Same as Swift

# app1 = JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied")
# print(app1.company)  # MSP A Co.
# print(app1.status)  # Applied

# Adding a Method
# class JobApplication:
#     def __init__(self, company, role, status):
#         self.company = company
#         self.role = role
#         self.status = status

#     def mark_rejected(self):
#         self.status = "Rejected"
#     def summary(self):
#         return f"{self.company} - {self.role} - {self.status}"

# app1 = JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied")
# print(app1.summary())

# app1.mark_rejected()
# print(app1.summary())

# Notice: every method takes self as its first parameter, even though you never pass it manually 
# when calling — Python does that automatically. This is the #1 "gotcha" for Swift devs: 
# you'll forget self and get errors like missing 1 required positional argument.

# self — why Python makes you write it explicitly
# In Swift, self is implicit inside instance methods — you can even often omit it entirely. 
# Python takes the opposite philosophy: nothing is hidden or implicit. Every method must 
# explicitly declare that it operates on an instance, via self as the first parameter. 
# This is described in Python's philosophy as "explicit is better than implicit."


# The __str__ method — controlling how print() displays your object
# class JobApplication:
#     def __init__(self, company, role, status):
#         self.company = company
#         self.role = role
#         self.status = status

#     def __str__(self):
#         return f"{self.company} - {self.role} - {self.status}"

# app1 = JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied")
# print(app1)

# Without __str__, print(app1) would show something unhelpful like <__main__.JobApplication object 
# at 0x104b2f...>. This is Python's rough equivalent of conforming to CustomStringConvertible 
# in Swift.


# Inheritance (same concept as Swift)
class Application:
    def __init__(self, company, role):
        self.company = company
        self.role = role

    def summary(self):
        return f"{self.company} - {self.role}"

class JobApplication(Application):
    def __init__(self, company, role, status):
        super().__init__(company, role) # Call the parent's __init__
        self.status = status

    def summary(self):
        return f"{self.company} - {self.role} - {self.status}"

# super() works exactly like Swift's super — accessing the parent class's version of 
# a method or initializer.


# A List of Objects (instead of list of dictionaries)
# Remember your capstone tracker used a list of dictionaries:
# applications = [
#     {"company": "MSP A Co.", "role": "...", "status": "Applied"},
#     ...
# ]

# Now, with classes, you'd use a list of objects instead:
applications = [
    JobApplication("MSP A Co.", "Sr. Solutions Engineer", "Applied"),
    JobApplication("MSP B Co.", "Sales Engineer", "Recruiter's Screening"),
    JobApplication("MSP C Co.", "Customer Success Engineer", "Interview 1")
]

for app in applications:
    print(app.summary())

# This is a meaningful upgrade — objects can carry behavior (methods like mark_rejected()), 
# while plain dictionaries only carry data.

