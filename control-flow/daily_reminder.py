# daily_reminder.py

task = input("Please enter a task description: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"High priority task: {task}. Please make sure to complete it as soon as possible."
    case "medium":
        reminder = f"Medium priority task: {task}. Try to get to it soon."
    case "low":
        reminder = f"Low priority task: {task}. You can handle it later."
    case _:
        reminder = "Invalid priority level entered. Please use 'high', 'medium', or 'low'."

if time_bound == "yes":
    reminder += " This requires immediate attention today!"

