queue = []

queue.append(5)
queue.append(10)
queue.append(15)
queue.append(20)

first_element = queue.pop(0)
print(f"{first_element}: first element")

print(queue)

# second option: thread-safe FIFO
from queue import Queue

queue = Queue()

queue.put(10)
queue.put(20)
queue.put(30)
queue.put(40)

first_element = queue.get()
print(f"{first_element}: first element")
print(queue.queue)
print(list[queue.queue])
