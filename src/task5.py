import asyncio
import time

async def function1():
    print("Function 1 - Start")
    await asyncio.sleep(1)
    print("Function 1 - Middle")
    await asyncio.sleep(4)
    print("Function 1 - End")

async def function2():
    print("Function 2 - Start")
    await asyncio.sleep(3)
    print("Function 2 - Middle 1")
    await asyncio.sleep(1)
    print("Function 2 - Middle 2")
    await asyncio.sleep(1)
    print("Function 2 - End")
