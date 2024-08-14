#In Python, a context manager is a construct that allows you to set up and
# clean up resources automatically. This is typically used with the with statement, 
# which ensures that resources are properly released after they are used, even if an 
# error occurs during their usage.


class MyContextManager:
    def __enter__(self):
        print("Entering the context...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context...")
        # Handle exceptions if needed
        return False  # Propagate exception if one occurred

# Using the custom context manager
with MyContextManager():
    print("Inside the context")
