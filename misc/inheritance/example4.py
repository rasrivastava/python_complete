"""
- If you call a method on a class with multiple parent classes, 
  Python follows the MRO to determine which method to execute.

- The method in the current class is called first.

- If super() is used, it follows the MRO to call the next method in the hierarchy.
"""

class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):
    def method(self):
        print("Method in D")
        super().method()
        #C.method(self)  # Call C's method directly --> Method in C

d = D()
d.method()

# Method in D
# Method in B

# The MRO for class D is: D -> B -> C -> A -> object