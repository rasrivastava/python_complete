import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(2)
    print("Task 1: End")
    return "Task 1 result"

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(1)
    print("Task 2: End")
    return "Task 2 result"

def main():
    loop = asyncio.get_event_loop()  # Get the current event loop
    
    # Schedule the tasks to run concurrently
    tasks = [task1(), task2()]
    
    # Run the tasks until they complete
    results = loop.run_until_complete(asyncio.gather(*tasks))
    
    print("Results:", results)

# Execute the main function
main()
