import asyncio


async def fetch_data() -> str:
    print('Fetching data...')

    # force for the program for waiting for the current function
    await asyncio.sleep(2.5)
    print("Data fetched!")

    return "API Data"


async def main():
    task = asyncio.create_task(
        fetch_data()
    )

    # task.cancel()

    # await asyncio.sleep(3)

    # print("Cancelled?", task.cancelled())

    try:
        # just wait for 2 seconds else Timeout error
        await asyncio.wait_for(task, timeout=2)

        if task.done():
            print("-", task.result())
        else:
            print("-", task.done())

        result = await task
        print(result)
    except asyncio.CancelledError:
        print("CANCELLED: Request was cancelled...")
    except asyncio.TimeoutError:
        print("TIMEOUT: Request took too long...")


if __name__ == "__main__":
    asyncio.run(main())