import asyncio
import random
import time


async def foo(param):
    await asyncio.sleep(random.randint(1, 3))

    # if param == 2:
    #     raise ValueError("My exception")

    print(f"start foo with param {param}")
    await asyncio.sleep(random.randint(1, 3))
    print(f"end foo with param {param}")
    return 10 * param


async def main():

    t1 = time.time()
    await asyncio.wait(
        [
            asyncio.create_task(foo(1)),
            asyncio.create_task(foo(2)),
            asyncio.create_task(foo(3)),
        ]
    )
    t2 = time.time()
    print(t2 - t1)


async def main2():

    t1 = time.time()
    results = await asyncio.gather(
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    )

    for result in results:
        print(result)

    t2 = time.time()
    print(t2 - t1)


async def main3():
    """
    обработка ошибок в цикле

    """
    t1 = time.time()

    tasks = [
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    ]

    for completed_task in asyncio.as_completed(tasks):
        try:
            await completed_task
        except ValueError:
            print(f"Caught ValueError in task {completed_task}")

    t2 = time.time()
    print(t2 - t1)


async def print_results():

    t1 = time.time()

    tasks = [
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    ]

    done, pending = await asyncio.wait(tasks)

    for task in tasks:
        print(task.result())

    t2 = time.time()
    print(t2 - t1)


async def dynamic_wait():
    t1 = time.time()
    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(foo(i)))

    await asyncio.wait(tasks)

    for task in tasks:
        print(task.result())

    t2 = time.time()
    print(t2 - t1)


async def dynamic_gather():
    t1 = time.time()
    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(foo(i)))

    await asyncio.gather(*tasks)

    for task in tasks:
        print(task.result())

    t2 = time.time()
    print(t2 - t1)


if __name__ == "__main__":
    asyncio.run(dynamic_gather())
