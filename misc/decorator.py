def decorator_definition(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decorator_definition
def decorator_imple():
    print("byeee")


decorator_imple()


import time

# Simple timing decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()       # before
        result = func(*args, **kwargs)
        end_time = time.time()         # after
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Function to reverse a string
@timing_decorator
def reverse_string(s):
    return s[::-1]

# Example usage
if __name__ == "__main__":
    print(reverse_string("Hello, World!"))
