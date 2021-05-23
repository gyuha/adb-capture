import asyncio
import aiofiles
from ppadb.client_async import ClientAsync as AdbClient


async def _save_screenshot(device):
    result = await device.screencap()
    file_name = f"{device.serial}.png"
    async with aiofiles.open(f"{file_name}", mode='wb') as f:
        await f.write(result)

    return file_name


async def main():
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = await client.devices()
    for device in devices:
        print(device.serial)

    result = await asyncio.gather(*[_save_screenshot(device) for device in devices])
    print(result)

asyncio.run(main())
