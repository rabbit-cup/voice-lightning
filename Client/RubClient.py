from testclient import Client

import asyncio


async def main():
    client = Client("ws://192.168.0.70:8080")
    await client.start_client()

if __name__ == "__main__":
    asyncio.run(main())