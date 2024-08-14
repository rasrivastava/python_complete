# Timeouts with wait_for():

# asyncio.wait_for() sets a timeout for an operation. 
# If the operation doesn't complete within the specified time, 
# it raises a TimeoutError

# await asyncio.wait_for(task1(), timeout=3.0)

import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(5)  # Pauses this coroutine for 5 seconds
    print("Task 1: End")
    return "Task 1 result"

async def main():
    try:
        # Run task1 with a timeout of 3 seconds
        result = await asyncio.wait_for(task1(), timeout=3.0)
        print(result)
    except asyncio.TimeoutError:
        print("Task 1 did not complete within the timeout period")

asyncio.run(main())

# Task 1: Start
# Task 1 did not complete within the timeout period
