import heapq

# second smallest element

aa = [6, 4, 3, 5, 2, 1]
k = 2 # second smallest element

q = []

for a in aa:
    heapq.heappush(q, a)

for i in range(k-1):
    heapq.heappop(q)

print(heapq.heappop(q))

# second highest element

aa = [6, 4, 3, 5, 2, 1]
k = 2 # second highest element

q = []

for a in aa:
    heapq.heappush(q, -a)

for i in range(k-1):
    -heapq.heappop(q)

print(-heapq.heappop(q))
