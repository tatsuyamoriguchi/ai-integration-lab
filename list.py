# 4. List comprehension (the fun one)
# Given daily_tasks = ["Job Apps", "SaaS Reach-Out", "Swimming", "eFax Reach-Out", "Python Study"], 
# use a list comprehension to create a new list containing only tasks that have the word "Reach-Out" in them.

# Loop version (not list comprehension!)
daily_tasks = ["Job Apps", "SaaS Reach-Out", "Swimming", "eFax Reach-Out", "Python Study"]
reach_out_tasks = []
for task in daily_tasks:
    if "Reach-Out" in task:
        reach_out_tasks.append(task)
print(reach_out_tasks)

# List Comprehension Version
dialy_tasks = ["Job Apps", "SaaS Reach-Out", "Swimming", "eFax Reach-Out", "Python Study"]
reach_out_tasks = [task for task in daily_tasks if "Reach-Out" in task]
print(reach_out_tasks)

no_reach_out_tasks = [task for task in daily_tasks if "Reach-Out" not in task]
print(no_reach_out_tasks)