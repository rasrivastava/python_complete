import threading
import time

# Create a Lock object to synchronize access to shared resources
print_lock = threading.Lock()

def print_hello():
    for _ in range(3):
        # Acquire the lock to ensure exclusive access to the print statement
        with print_lock:
            print("Hello from thread")
        # Release the lock and sleep for 1 second
        time.sleep(1)

def print_world():
    for _ in range(3):
        # Acquire the lock to ensure exclusive access to the print statement
        with print_lock:
            print("World from thread")
        # Release the lock and sleep for 1 second
        time.sleep(1)

# Create threads to run the print_hello and print_world functions
thread1 = threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_world)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete before proceeding
thread1.join()
thread2.join()

"""
Hello from thread
World from thread
Hello from thread
World from thread
Hello from thread
World from thread
"""