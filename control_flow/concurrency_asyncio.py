import asyncio
import time
MAX_WORKERS = 20


@asyncio.coroutine
def double_one(multiplier):
    result = 2 * multiplier
    try:
        yield from asyncio.sleep(multiplier)
    except TypeError:
        return TypeError
    print(result)
    return result


async def double_one_async(multiplier):
    result = 2 * multiplier
    try:
        await asyncio.sleep(multiplier)
    except TypeError:
        return TypeError
    print(result)
    return result


def double_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [double_one_async(cc) for cc in cc_list]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    if any([item.result() == TypeError for item in iter(res)]):
        return "Non number found"
    return "Doubled all"
