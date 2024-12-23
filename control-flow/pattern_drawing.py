# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Check if the user input is a positive integer
if size > 0:
    # Use a while loop to iterate through each row
    row = 1
    while row <= size:
        # Inside the while loop, use a for loop to print asterisks side by side
        for col in range(size):
            print("*", end="")  # Print '*' without moving to a new line
        print()  # Print a newline after each row
        row += 1  # Increment the row number to move to the next row
else:
    print("Please enter a positive integer.")

