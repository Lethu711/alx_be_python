# daily_reminder.py

# Prompt for user input
task = input("Enter your task description: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes/no): ").lower()

# Process the task based on priority using a Match Case statement
match priority:
    case "high":
        reminder = f"Your task '{task}' has a high priority."
    case "medium":
        reminder = f"Your task '{task}' has a medium priority."
    case "low":
        reminder = f"Your task '{task}' has a low priority."
    case _:
        reminder = f"Your task '{task}' has an unknown priority."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " That requires immediate attention today!"

# Output the customized reminder
print(reminder)

