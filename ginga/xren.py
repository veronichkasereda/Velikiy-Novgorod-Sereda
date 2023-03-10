import asyncio
import time


async def run_task(name, *args):
    COEF = 0.01
    times = [(args[0], args[1]), (args[2], args[3])]
    for n, (t1, t2) in enumerate(times, 1):
        print(f'{name} started the {n} task.')
        await asyncio.sleep(COEF * t1)
        print(f'{name} moved on to the defense of the {n} task.')
        await asyncio.sleep(COEF * t2)
        print(f'{name} completed the {n} task.')


async def interviews_2(*data):
    task = []
    for elem in data:
        task.append(run_task(*elem))
    await asyncio.gather(*task)


if __name__ == '__main__':
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews_2(*data))
    print(time.time() - t0)