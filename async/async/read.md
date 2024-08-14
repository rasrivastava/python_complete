## Coroutines

- Coroutines are a type of `asynchronous function` in Python that can be `paused` and `resumed`, allowing for `concurrent execution`.

- They are a fundamental concept in `asynchronous programming` and are `used to` write code that `can handle I/O operations`, `tasks`, or `other long-running` operations `without blocking` the `execution of the program`.

### Basic Definition:

- A `coroutine` is defined using the `async def` syntax in Python.
- It can use the `await` keyword to `pause its execution` until the `awaited coroutine` or `future is complete`.

## Key Characteristics:

- `Async Functions`:
   - Coroutines are typically defined with async def, making them asynchronous functions.
- `Await Expression`
   - Within a coroutine, the await keyword is used to pause execution until another coroutine or asynchronous operation completes.
- `Event Loop`: Coroutines are managed by an event loop, which schedules and runs them.

```
import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(3)  # Simulates a long-running task
    print("Task 1: End")
    return "Task 1 result"

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(1)  # Simulates a shorter task
    print("Task 2: End")
    return "Task 2 result"

async def main():
    print("Main: Start")
    # Schedule tasks concurrently
    results = await asyncio.gather(task1(), task2())
    print("Results:", results)
    print("Main: End")

# Run the main coroutine using the event loop
asyncio.run(main())
```

- **Coroutines Definition**:
  - `task1` and `task2` are asynchronous functions (coroutines) that use await to simulate waiting for asynchronous operations to complete.

- **Event Loop Execution**:
  - `asyncio.run(main())` starts the event loop and executes the main coroutine.
  - Inside main, `asyncio.gather(task1(), task2())` schedules task1 and task2 to run concurrently.

- **Task Scheduling and Execution**:
  - The `event loop` `starts executing` `task1` and `task2`.
  - `task2` completes before `task1` because it has a shorter sleep duration.
  - During the sleep period of `task1`, the event loop switches to execute `task2` and then returns to `task1` when `task2` completes.


- `gather()`:
   - when you have multiple coroutines that need to run concurrently and you want to gather their results in a single operation.

   ```
   async def main():
      results = await asyncio.gather(task1(), task2())
      print(results)  # Output: ['Result 1', 'Result 2']
   ```

- `asyncio.create_task()`:
   - asyncio.create_task() schedules a coroutine to run     concurrently and returns an asyncio.Task object.
   - This method is useful for starting and managing individual coroutines.

   ```
   async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    
    result1 = await t1
    result2 = await t2
    
    print(result1, result2)
   ```
   - `Characteristics`:
    - `Return Type`: Returns an asyncio.Task object.
    - `Error Handling`: **Tasks need to be managed individually**; **exceptions need to be handled for each task separately**.
    - `Control`: Provides granular control over each task, including starting, cancelling, and handling exceptions.

- `asyncio.TaskGroup` (`Python 3.11+`)
  - **Purpose**:
    - `asyncio.TaskGroup` provides structured concurrency, allowing you to manage multiple tasks with automatic lifecycle management and error handling.
    - It ensures that all tasks are awaited and cleaned up properly when the group exits.

  - **Usage**:
    - Use `asyncio.TaskGroup` when you want to manage multiple tasks collectively with automatic cleanup and error handling.

    ```
    async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(task1())
        t2 = tg.create_task(task2())
    
    result1 = await t1
    result2 = await t2
    print(result1, result2)
    ```

## Summary of Differences


### Purpose:

- `asyncio.gather()`
  - Aggregates multiple coroutines and returns their results as a list.
- `asyncio.create_task()`
  - Schedules individual coroutines for concurrent execution, returning an asyncio.Task object.
- `asyncio.TaskGroup`
  - Manages multiple tasks with structured concurrency, handling their lifecycle and errors collectively.


### Return Type:

- `asyncio.gather()`: Returns a coroutine that resolves to a list of results.

- `asyncio.create_task()`: Returns an asyncio.Task object.

- `asyncio.TaskGroup`: Manages tasks within its scope and ensures they are completed.


## Control:

- `asyncio.gather()`: Aggregates results but provides less control over individual tasks.

- `asyncio.create_task()`: Provides granular control over individual tasks, including their start, cancellation, and error handling.

- `asyncio.TaskGroup`: Provides high-level management of multiple tasks with automatic lifecycle management.


## Error Handling:

- `asyncio.gather()`: Exceptions are propagated and can be managed with return_exceptions=True.

- `asyncio.create_task()`: Exceptions need to be handled individually for each task.

- `asyncio.TaskGroup`: Handles exceptions collectively, ensuring all tasks are completed.