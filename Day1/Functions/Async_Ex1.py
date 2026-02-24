import asyncio

async def async_function():
    print("Starting the async function.")
    await asyncio.sleep(2)  # Non blocking sleep
    print("This is an async function.")
    print("It executes aynchronously.")

asyncio.run(async_function())
print("Program Finished")