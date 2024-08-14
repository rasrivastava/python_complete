import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_hello())

asyncio.run(main())

######################################################

import threading
import time

def say_hello():
    print("Hello")
    time.sleep(1)
    print("World")

thread1 = threading.Thread(target=say_hello)
thread2 = threading.Thread(target=say_hello)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
