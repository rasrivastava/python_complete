import threading
import time

def print_hello():
    for _ in range(3):
        print("Hello from thread")
        time.sleep(1)

def print_world():
    for _ in range(3):
        print("World from thread")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_world)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution")

"""
Hello from thread
World from thread
Hello from thread
World from thread
Hello from thread
World from thread
Both threads have finished execution
"""