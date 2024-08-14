def divide(a, b):
    try:
        result = a / b
        print("Division successful.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
        result = None  # Initialize result in case of an exception
    finally:
        print("Cleaning up resources.")
    return result

#print(divide(10, 2))  # Expected to return 5.0
print(divide(10, 0))  # Expected to handle division by zero
