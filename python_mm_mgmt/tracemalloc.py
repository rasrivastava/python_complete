import tracemalloc

tracemalloc.start()

# Code block to track
list_of_numbers = [i for i in range(100000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
