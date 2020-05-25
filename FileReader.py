import asyncio
from aioavast import Avast

@asyncio.coroutine
def scan(item):
    av = Avast()
    yield from av.connect()
    return (yield from av.scan(item))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(scan('/home/fractaluser/Desktop/PythonScripts/DirectoryExplorer.py'))
    print(results)

