In Python, memory management involves two types of memory allocations: stack memory and heap memory. Understanding the difference between these two can help in writing more efficient code and avoiding memory-related issues.

Stack Memory
Usage: Stack memory is used for static memory allocation, which includes function calls, local variables, and control flow.
Characteristics:
Size: Limited and typically smaller compared to heap memory.
Lifespan: Variables are created when a function is called and destroyed when the function exits.
Speed: Faster access compared to heap memory due to its LIFO (Last In, First Out) structure.
Scope: Limited to the function in which they are created.

Heap Memory
Usage: Heap memory is used for dynamic memory allocation, which includes objects and data that need to persist beyond a single function call.
Characteristics:
Size: Larger compared to stack memory and can grow dynamically.
Lifespan: Variables exist until they are explicitly deleted or garbage collected.
Speed: Slower access compared to stack memory due to the complexity of dynamic allocation and deallocation.
Scope: Accessible from anywhere in the program.

## Stack Memory Example

```
def stack_example():
    x = 10  # Local variable stored in stack memory
    y = 20  # Another local variable in stack memory
    return x + y  # The function uses stack memory for local variables and function calls

result = stack_example()
print(result)  # Output: 30
```

- In this example, x and y are local variables stored in stack memory. They are created when the stack_example function is called and destroyed when the function exits.

## Heap Memory Example
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list():
    head = Node(1)  # Node object stored in heap memory
    second = Node(2)  # Another Node object in heap memory
    head.next = second  # Linking nodes
    return head

linked_list = create_linked_list()
print(linked_list.value)  # Output: 1
print(linked_list.next.value)  # Output: 2
```

- In this example, instances of the Node class are stored in heap memory. They persist beyond the function call and are accessible from anywhere in the program until explicitly deleted or garbage collected.

Summary
- `Stack Memory`:
   - Used for static memory allocation
   - faster access
   - limited scope and lifespan
   - typically used for function calls and local variables.

- `Heap Memory`:
  - Used for dynamic memory allocation
  - slower access
  - larger size
  - persists beyond function calls
  - typically used for objects and dynamic data.