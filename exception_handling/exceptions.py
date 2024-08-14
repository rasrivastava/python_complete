# Basic Syntax
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero!")

# Handling Multiple Exceptions
try:
    # Code that might raise an exception
    result = int("not a number")
except ValueError:
    print("ValueError: Invalid conversion")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")

# Catching All Exceptions
try:
    # Code that might raise an exception
    result = 10 / 0
except Exception as e:
    # Handle all exceptions
    print(f"An error occurred: {e}")


# Else Block

# The else block, if present, is executed if no exceptions
# were raised in the try block:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")


# finally Block

# The finally block, if present, is always executed,
# regardless of whether an exception was raised or not.
# It’s often used for cleanup actions:

try:
    file = open('file.txt', 'r')
    # Read file content
finally:
    file.close()
    print("File closed")

