class A:
    def method(self):
        print("Method in A")

class B(A):
    pass

b = B()
b.method()  # Output: "Method in A"
