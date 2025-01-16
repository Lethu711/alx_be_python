# robust_division_calculator.py
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num/den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input detected. Please enter valid numbers."
    except Exception as e:
        return f"Unexpected error: {str(e)}"

