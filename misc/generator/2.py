"""
Generator Function
A generator function is defined like a normal function but uses
the yield keyword to return values one at a time.

Example: Fibonacci Sequence Generator
"""

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num)

"""
0
1
1
2
3
5
8
"""