# explore_datetime.py

import datetime

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()
    
    # Format and print the current date and time in "YYYY-MM-DD HH:MM:SS"
    print("Current Date and Time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    while True:
        try:
            # Prompt the user to enter the number of days
            number_of_days = int(input("Enter the number of days to add to the current date: "))
            break  # Exit loop if the input is a valid integer
        except ValueError:
            print("Invalid input! Please enter an integer value.")
    
    # Calculate the future date by adding the specified number of days
    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    
    # Print the future date in "YYYY-MM-DD" format
    print("Future Date: ", future_date.strftime("%Y-%m-%d"))

# Call functions to demonstrate functionality
if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

