from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    print("Current Date and Time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    while True:
        try:
            number_of_days = int(input("Enter the number of days to add to the current date: "))
            break  # Exit loop if valid input is provided
        except ValueError:
            print("Invalid input! Please enter an integer value.")
    
    # Calculate the future date by adding the number of days
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    
    print("Future Date: ", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

