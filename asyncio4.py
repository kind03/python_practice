import asyncio


async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    task = asyncio.create_task(nested())

    # Let's do it differently now and await it:
    print(await task)  # will print "42".

asyncio.run(main())