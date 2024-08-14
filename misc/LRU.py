from collections import deque

class LRUCache:
    # Initialize cache
    def __init__(self, n):
        self.csize = n
        self.dq = deque()
        self.ma = {}

    # Refers key x with in the LRU cache
    def refer(self, x):
        # If not present in cache
        if x not in self.ma:
            # Cache is full
            if len(self.dq) == self.csize:
                # Remove least recently used element from deque and map
                last = self.dq.pop() # remove the last value
                del self.ma[last]    # remove the key, val from ma={} as well
        else:
            # Remove the element from deque to update its position
            self.dq.remove(x)

        # Insert the element at the front and update the map
        self.dq.appendleft(x)
        self.ma[x] = True

    # Function to display contents of cache
    def display(self):
        # Display all the elements in the deque
        print(list(self.dq))


# Driver Code
ca = LRUCache(4)

ca.refer(1)  # [1]
ca.refer(2)  # [2, 1]
ca.refer(3)  # [3, 2, 1]
ca.refer(1)  # [1, 3, 2]
ca.refer(4)  # [4, 1, 3, 2]
ca.refer(5)  # [5, 4, 1, 3]
ca.display()

####

# initial setup

# csize = 4
# dq = []
# ma = {}

# operations

# ca.refer(1)
# dq = [1] , ma {1: True}

# ca.refer(2)
# dq = [2, 1] , ma {1: True, 2: True}

# ca.refer(3)
# dq = [3, 2, 1] , ma {1: True, 2: True, 3: True}

# ca.refer(1) --> 1 is already there
# dq = [1, 3, 2] , ma {1: True, 2: True, 3: True}

# ca.refer(4)
# dq = [4, 1, 3, 2] , ma {1: True, 2: True, 3: True, 4: True}

# ca.refer(5)
# dq = [5, 4, 1, 3] , ma {1: True, 2: True, 3: True, 5: True}

# final state:
# dq = [5, 4, 1, 3]
# ma {1: True, 2: True, 3: True, 5: True}