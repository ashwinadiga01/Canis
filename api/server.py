import asyncio
import websockets
import random


def getRandomNum():
    return str(random.uniform(980, 1000))

def getRandomPercent():
    return str(random.uniform(-1.3, 1.9))

def getData():
    
    data =[
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "11483",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1594",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1922",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "4963",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "2885",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "11536",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1333",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1330",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1394",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1160",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "10666",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "11536",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "21238",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "5900",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "3045",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1023",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "5258",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "2263",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "18391",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "11184",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "13538",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "236",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "7229",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "3506",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "317",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "10604",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "16675",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "1660",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltq": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            "tk": "3787",
            'cng': getRandomPercent(),
            'nc': getRandomPercent()
        },
        {
            'c': getRandomNum(),
            'cng': getRandomPercent(),
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            'nc': getRandomPercent(),
            "tk": "26000"
        },
        {
            'c': getRandomNum(),
            'cng': getRandomPercent(),
            "e": "nse_cm",
            "ltp": getRandomNum(),
            "ltt": "NA",
            "name": "sf",
            'nc': getRandomPercent(),
            "tk": "26009"
        }
    ]
    return str(data)


async def hello(websocket):
    await websocket.send(getData())

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())