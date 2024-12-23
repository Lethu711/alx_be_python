# daily_reminder.py

# Prompt for task description
task = input("Please enter a task description: ").strip()

# Prompt for priority level and check if it is valid
priority = input("Enter the priority of the task (high, medium, low): ").strip().lower()
while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter 'high', 'medium', or 'low'.")
    priority = input("Enter the priority of the task (high, medium, low): ").strip().lower()

# Prompt for time-bound status and check if it's valid
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()
while time_bound not in ["yes", "no"]:
    print("Invalid response! Please enter 'yes' or 'no'.")
    time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"High priority task: {task}. Please make sure to complete it as soon as possible."
    case "medium":
        reminder = f"Medium priority task: {task}. Try to get to it soon."
    case "low":
        reminder = f"Low priority task: {task}. You can handle it later."
    case _:
        reminder = "Error: Invalid priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Provide a customized reminder and print it
print(reminder)

