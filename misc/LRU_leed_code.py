class Node:
    def __init__(self, key: int, value: int):
        self.key = key  # The key of the cache entry
        self.value = value  # The value of the cache entry
        self.prev = None  # Pointer to the previous node in the linked list
        self.next = None  # Pointer to the next node in the linked list

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # The maximum capacity of the cache
        self.cache = {}  # Dictionary to store key-node pairs for O(1) access
        # Initialize a dummy head and tail node to simplify adding/removing nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # Connect the head and tail to each other initially
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove an existing node from the linked list."""
        prev_node = node.prev  # Get the previous node
        next_node = node.next  # Get the next node
        prev_node.next = next_node  # Link the previous node to the next node
        next_node.prev = prev_node  # Link the next node back to the previous node

    def _add(self, node: Node):
        """Add a new node right after the head."""
        next_node = self.head.next  # Get the node currently after the head
        node.next = next_node  # Point the new node to the current first node
        node.prev = self.head  # Link the new node back to the head
        self.head.next = node  # Point the head to the new node
        next_node.prev = node  # Link the old first node back to the new node

    def get(self, key: int) -> int:
        if key in self.cache:  # Check if the key is in the cache
            node = self.cache[key]  # Retrieve the node corresponding to the key
            self._remove(node)  # Remove the node from its current position
            self._add(node)  # Add the node to the front (marking it as recently used)
            return node.value  # Return the value of the node
        return -1  # If the key is not found, return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # If the key is already in the cache
            self._remove(self.cache[key])  # Remove the old node from the linked list
        # Create a new node with the key and value
        node = Node(key, value)
        self._add(node)  # Add the new node to the front of the linked list
        self.cache[key] = node  # Update the cache with the new node
        if len(self.cache) > self.capacity:  # If the cache exceeds its capacity
            # Remove the LRU element (node just before the tail)
            lru = self.tail.prev
            self._remove(lru)  # Remove the LRU node from the linked list
            del self.cache[lru.key]  # Remove the corresponding entry from the cache

# Example usage:
# Instantiate an LRUCache object and perform operations as shown in the problem statement.

# Driver Code
lru_cache = LRUCache(2)
print(lru_cache.put(1, 1))  # Cache: {1=1}
print(lru_cache.put(2, 2))  # Cache: {1=1, 2=2}
print(lru_cache.get(1))     # Returns 1, Cache: {2=2, 1=1}
print(lru_cache.put(3, 3))  # Cache: {1=1, 3=3}, evicts key 2
print(lru_cache.get(2))     # Returns -1 (not found)
print(lru_cache.put(4, 4))  # Cache: {3=3, 4=4}, evicts key 1
print(lru_cache.get(1))     # Returns -1 (not found)
print(lru_cache.get(3))     # Returns 3, Cache: {4=4, 3=3}
print(lru_cache.get(4))     # Returns 4, Cache: {3=3, 4=4}
