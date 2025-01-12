# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor from Celsius to Fahrenheit

# Conversion function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Conversion function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main user interaction section
def main():
    try:
        # Ask the user to input the temperature value with unit (Celsius or Fahrenheit)
        temperature_input = input("Enter the temperature value (e.g., 100 or 100F or 100C): ").strip()

        # Ensure the input isn't empty
        if not temperature_input:
            raise ValueError("Input cannot be empty.")

        # Check if input ends with 'F' (Fahrenheit) or 'C' (Celsius)
        if temperature_input[-1].upper() == 'F':  # Fahrenheit input
            temperature_value = float(temperature_input[:-1].strip())  # Extract numeric part
            converted_temp = convert_to_celsius(temperature_value)
            print(f"{temperature_value}°F is equal to {converted_temp:.2f}°C.")
        elif temperature_input[-1].upper() == 'C':  # Celsius input
            temperature_value = float(temperature_input[:-1].strip())  # Extract numeric part
            converted_temp = convert_to_fahrenheit(temperature_value)
            print(f"{temperature_value}°C is equal to {converted_temp:.2f}°F.")
        else:  # Invalid input
            raise ValueError("Invalid temperature. Please enter a numeric value with 'C' or 'F' at the end.")
    
    except ValueError as ve:
        # Handle invalid numeric inputs and other value errors
        print(f"Error: {ve}")
    except IndexError:
        # Handle cases where the input is empty or ends unexpectedly
        print("Error: Input is empty or improperly formatted.")

if __name__ == "__main__":
    main()

