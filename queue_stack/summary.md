1. Queue:

- Insertion (enqueue): 𝑂(1)
- Deletion (dequeue): 𝑂(1)
- Update: Not applicable; queues typically do not support direct update operations.
- Find: Not applicable; queues typically do not support direct access or search operations.

2. Deque (collections.deque)

- Insertion (append): O(1) (at both ends)
- Deletion (pop): O(1) (at both ends)
- Update: O(n) for updating an element at an arbitrary position (requires searching)
- Find: O(n) for finding an element in an arbitrary position (requires searching)

3. Priority Queue (queue.PriorityQueue)

- Insertion: O(logn)
- Deletion: O(logn)
- Update: Not directly supported; usually involves removing and re-inserting elements.
- Find: O(n) for linear search (not typically optimized for direct access by index)
