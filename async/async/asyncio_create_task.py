import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(3)
    print("Task 1: End")
    return "Task 1 result"

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(1)
    print("Task 2: End")
    return "Task 2 result"

async def main():
    # Create tasks
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    
    # Await tasks separately
    result1 = await t1
    result2 = await t2

    print("Results:", result1, result2)

asyncio.run(main())
