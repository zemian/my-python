# Python version of explaining Event and Wait process
# https://stackoverflow.com/questions/68139555/difference-between-async-await-in-python-vs-javascript
#
import asyncio

# This async function will resolve
# after the number of ms provided has passed
async def wait_game(ms):
    await asyncio.sleep(ms / 1000)

async def my_main():
    print(2)
    await wait_game(100)
    print(4)

async def my_concurrent_step():
    print(3)

async def main():
    # Compare this to JavaScript, we must create two tasks and run them in parallel
    print(1)
    task1 = asyncio.create_task(my_main())
    task2 = asyncio.create_task(my_concurrent_step())
    await asyncio.gather(task1, task2)

# Python 3.7+
asyncio.run(main())