import sys

# Create an object
x = [1, 2, 3] # Reference count is 1 (from the variable x)

# Get reference count
ref_count_before = sys.getrefcount(x) # Reference count is 2 (variable x + temporary reference inside getrefcount)

print("Reference count before setting x to None:", ref_count_before)
# Reference count before setting x to None: 2

# Assign another variable to hold the reference to the list
y = x

x = None

# Get reference count again using y
ref_count_after = sys.getrefcount(y)  # Reference count should be 2 (variable y + temporary reference inside getrefcount)

print("Reference count after setting x to None:", ref_count_after)  # Prints 2
#Reference count after setting x to None: 2

## second example

import sys

# Create an object
x = [1, 2, 3]
print(sys.getrefcount(x))  # Output: 2 (x and the argument to getrefcount)

# Create another reference
y = x
print(sys.getrefcount(x))  # Output: 3 (x, y, and the argument to getrefcount)

# Remove a reference
del y
print(sys.getrefcount(x))  # Output: 2 (x and the argument to getrefcount)


import gc

# Print current thresholds
print(gc.get_threshold()) # (700, 10, 10)

# Manually trigger garbage collection
gc.collect()

# Print statistics about garbage collection
print(gc.get_stats())
# [{'collections': 7, 'collected': 24, 'uncollectable': 0}, {'collections': 0, 'collected': 0, 'uncollectable': 0}, {'collections': 1, 'collected': 0, 'uncollectable': 0}]