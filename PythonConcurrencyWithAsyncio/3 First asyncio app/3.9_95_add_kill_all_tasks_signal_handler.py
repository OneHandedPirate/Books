import asyncio
import signal
from asyncio import AbstractEventLoop

from utils import delay


def cancel_tasks():
    print("SIGINT signal received!")
    tasks: set[asyncio.Task] = asyncio.all_tasks()

    print(f"Remove {len(tasks)} task(s)")
    [task.cancel() for task in tasks]


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)

    await delay(10)


asyncio.run(main())
