# (push and pop) with 𝑂(1) time complexity

from collections import deque

queue = deque()

queue.append(5)
queue.append(10)
queue.append(15)
queue.append(20)

last_element = queue.pop()
print(f"{last_element}: last element")
print(queue)

first_element = queue.popleft()
print(f"{first_element}: first element")
print(queue)

add_to_right = queue.append(100)
print(queue)

add_to_ledt = queue.appendleft(0)
print(queue)