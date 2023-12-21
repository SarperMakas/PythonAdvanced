import asyncio

async def fetch_data() -> str:
    print('Fetching data...')

    # force for the program for waiting for the current function
    await asyncio.sleep(2.5)
    print("Data fetched!")

    return "API Data"

async def send_data(to: str):
    print(f"Sending data to {to}...")
    await asyncio.sleep(2)
    print(f"Data sent to {to}!")

async def main():
    data = await fetch_data()
    print("Data:", data)

    # use functions at the same time
    await asyncio.gather(send_data("Mario"), send_data("Luigi"))


if __name__ == "__main__":
    asyncio.run(main())