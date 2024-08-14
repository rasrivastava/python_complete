import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(5)  # Pauses this coroutine for 5 seconds
    print("Task 1: End")

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(2)  # Pauses this coroutine for 2 seconds
    print("Task 2: End")

async def main():
    # Running both tasks concurrently
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Task 1: Start
# Task 2: Start
# Task 2: End
# Task 1: End