import asyncio
import websockets
import random


def getRandomNum():
    return str(random.uniform(980, 1000))

def getRandomPercent():
    return str(random.uniform(-5, -5))

def getData():
    data = [
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1333",
            'cng': getRandomPercent(),
            'nc': getRandomPercent(),
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "11536",
            'cng': getRandomPercent(),
            'nc': getRandomPercent(),
        },
        {
            'c': getRandomNum(),
            'cng': getRandomPercent(),
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            'nc': getRandomPercent(),
            "tk": "26000",
        },
        {
            'c': getRandomNum(),
            'cng': getRandomPercent(),
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            'nc': getRandomPercent(),
            "tk": "26009",
        },
    ]
    return str(data)


async def hello(websocket):
    await websocket.send(getData())

def koibhi():
    while True:
        return getData()

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())