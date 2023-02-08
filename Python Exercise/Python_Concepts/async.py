import asyncio


async def function_1():
    print("A")
    await asyncio.sleep(3)
    print("B")


async def function_2():
    print(1)
    await function_3()
    print(2)


async def function_3():
    print("**")
    await asyncio.sleep(2)
    print("--")


asyncio.run(function_1())
asyncio.run(function_2())
