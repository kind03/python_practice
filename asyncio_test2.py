import asyncio


async def a():
    print('Suspending a')
    await asyncio.sleep(0)
    print('Resuming a')


async def b():
    print('In b')


def c():
    print('Inner C')
    return 12


async def main():
    await asyncio.gather(a(), b())
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    future: asyncio.Future = loop.run_in_executor(None, c)
    print(future.done())
    await future
    print(future.done())


if __name__ == '__main__':
    asyncio.run(main())
