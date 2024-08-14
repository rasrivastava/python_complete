# Memory Management in Python

- Understanding Memory allocation is important to any software developer as writing efficient code means writing a memory-efficient code.

- Memory allocation can be defined as allocating a block of space in the computer memory to a program.

- In Python memory allocation and deallocation method is automatic as the Python developers created a garbage collector for Python so that the user does not have to do manual garbage collection.

- Python’s memory allocation and deallocation method is automatic.
- The user does not have to preallocate or deallocate memory similar to using dynamic memory allocation in languages such as C or C++. 

- Python uses two strategies for memory allocation: 
  - Reference counting
  - Garbage collection

# Reference counting

- Python and various other programming languages employ reference counting, a memory management approach, **to automatically manage memory by tracking how many times an object is referenced**.
- A reference count, or the number of references that point to an object, is a property of each object in the Python language.
- **When an object’s reference count reaches zero, it becomes un-referenceable and its memory can be freed up.**


# Garbage collection

- Garbage collection (GC) in Python is the process of automatically detecting and reclaiming memory that is no longer in use, thereby preventing memory leaks and optimizing memory usage.

- Python employs a combination of reference counting and a cyclic garbage collector to manage memory.

- Here’s a detailed overview of how garbage collection works in Python:
  - Reference Counting
  -  Cyclic Garbage Collection

### 1. Reference Counting

- Reference counting is the primary memory management technique in Python.
- Each object maintains a count of references pointing to it.
- The main points to understand about reference counting are:
  - **Incrementing Count**: `The reference count increases when a new reference to the object is created.`
  - **Decrementing Count**: `The reference count decreases when a reference to the object is deleted or goes out of scope.`
  - **Deallocation**: `When the reference count drops to zero, the memory occupied by the object is deallocated immediately.`

```
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
```

### 2. Cyclic Garbage Collection

- Reference counting alone cannot handle cyclic references (where objects reference each other, forming a cycle).
- Python uses a cyclic garbage collector to detect and collect these cycles.
- The cyclic garbage collector works in conjunction with reference counting.

 - `How Cyclic Garbage Collection Works:`
    - `Generational Approach`:
       - **Python’s garbage collector divides objects into three generations (0, 1, and 2).**
       - **New objects start in the youngest generation (0).**
       - ***Objects that survive garbage collection cycles are promoted to older generations.**
    - `Triggering Collection`:
       - **Collection is triggered when the number of allocations minus the number of deallocations exceeds a certain threshold.**
       - **The collection frequency is higher for younger generations.**
    - `Mark and Sweep`:
       - **The garbage collector uses a mark-and-sweep algorithm to detect cycles.**
       - **It marks all objects reachable from the root and then sweeps (deletes) the unmarked objects, which are considered unreachable and hence garbage.**

### 3. Using the gc Module

- The gc module in Python provides an interface to the garbage collector, allowing developers to interact with and control garbage collection.

- Common Functions in the gc Module:
  - `gc.collect([generation])`: Manually triggers garbage collection. If no generation is specified, it collects all generations.
  - `gc.get_threshold()`: Returns the current collection thresholds.
  - `gc.set_threshold(threshold0, threshold1, threshold2)`: Sets the collection thresholds for the three generations.
  - `gc.get_count()`: Returns the current number of objects in each generation.
  - `gc.get_stats()`: Provides statistics about the garbage collection process

```
import gc

# Print current thresholds
print(gc.get_threshold()) # (700, 10, 10)

# Manually trigger garbage collection
gc.collect()

# Print statistics about garbage collection
print(gc.get_stats())
# [{'collections': 7, 'collected': 24, 'uncollectable': 0}, {'collections': 0, 'collected': 0, 'uncollectable': 0}, {'collections': 1, 'collected': 0, 'uncollectable': 0}]
```

### 4. Managing Garbage Collection

- Sometimes, it may be necessary to manage garbage collection to optimize performance, especially in performance-critical applications.

```
import gc

# Disable garbage collection
gc.disable()

# Perform memory-intensive operations

# Enable garbage collection
gc.enable()

# Manually trigger a collection
gc.collect()
```

### 5. Dealing with Cyclic References

- To avoid cyclic references, it’s often helpful to use weak references.
- The weakref module allows the creation of weak references, which do not increase the reference count of an object. This way, even if a cycle is formed, the garbage collector can collect the objects.

```
import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

# Create an object
obj = MyClass(10)

# Create a weak reference to the object
weak_obj = weakref.ref(obj)

# Access the object through the weak reference
print(weak_obj().value)  # Output: 10

# Delete the strong reference
del obj

# The weak reference returns None, as the object has been garbage collected
print(weak_obj())  # Output: None
```

### Summary
- Garbage collection in Python is a robust system that combines reference counting and cyclic garbage collection to manage memory efficiently.
- Understanding and utilizing the gc module and weak references can help developers optimize memory usage and manage the lifecycle of objects in complex applications.

