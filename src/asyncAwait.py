import asyncio
import time
from datetime import datetime

# python does not have a built-in async system or a event loop by default
# hene all code is executed from top to bottom. All executions are blocking
# and the code will not continue until the current line is executed
start = time.perf_counter()
time.sleep(10)  # Sleeps for 1 second
end = time.perf_counter()
print(f"Sync Elapsed time: {end - start} seconds")

async def async_function_one():
    print("async_function_one started")
    await asyncio.sleep(2)  # Simulate a non-blocking sleep. until the await is called, the function is not executed
    print("async_function_one finished")

# inside an aync function, it may not have a await
# but if there is an await, it is mandatory to be an async function
async def async_function_two():
    print("async_function_two started")
    
async def async_function():
    await async_function_one()
    start = time.perf_counter()
    await asyncio.sleep(5)
    end = time.perf_counter()
    print(f"async Elapsed time:  {end - start} seconds")
    print("async done insdie function")


print("\n")

start = time.perf_counter()
asyncio.run(async_function()) # creates the event loop and run BLOCKING.

#below code is blocked until the event loop is finished
print("done in module")
end = time.perf_counter()
print(f"Elapsed time: {end - start} seconds")