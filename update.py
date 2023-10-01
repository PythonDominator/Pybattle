from create import update, update_player, update_weather
from movement import key_up, key_down, keys_pressing
import asyncio
from element import Element, document
from pyodide.ffi import create_proxy


async def myLongFunction():
    while True:
        await update_weather()
        await update_player()
        await update()
        await asyncio.sleep(0.07)


document.onkeydown = create_proxy(key_down)
document.onkeyup = create_proxy(key_up)

asyncio.ensure_future(myLongFunction())


def get_dir_func(c):
    def y(_):
        async def x():
            keys_pressing.add(c)
            await asyncio.sleep(0.05)
            keys_pressing.remove(c)

        asyncio.ensure_future(x())

    return create_proxy(y)


Element("up").add_event("click", get_dir_func("w"))


Element("left").add_event("click", get_dir_func("a"))


Element("down").add_event("click", get_dir_func("s"))


Element("right").add_event("click", get_dir_func("d"))
