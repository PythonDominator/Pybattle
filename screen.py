import os
import time
import constants
from textwrap3 import wrap
import win32api

def clear() -> None:
    os.system('cls')

def typewrite(text: str, delay: float = constants.NORMAL_DELAY_TIME, skip: bool = True,
              end_delay: float = constants.END_DELAY_TIME, clears: bool = True, color = None, 
              skip_delay: float = constants.SKIP_DELAY_TIME) -> None:
    propertys = ''
    if color != None:
        propertys += color
            
    lines = wrap(text)
    for line in lines:
        line += '\n'
        for index, char in enumerate(line):
            if skip:
                if win32api.GetKeyState(0x20) < 0:
                    print(f'{propertys}{line[index:]}', end='')
                    time.sleep(skip_delay)
                    break
            
            print(f'{propertys}{char}', end='')
            if char == '.' or char == '!':
                time.sleep(end_delay)
            else:
                time.sleep(delay)
            
    if clears:
        clear()
            
def restricted_input(text: str, keys: list[str], delay: float = constants.INPUT_DELAY, type_write: bool = False) -> str:
    hex_keys = []
    for key in keys:
        if key == '1':
            hex_keys.append(0x31)
        if key == '2':
            hex_keys.append(0x32)
        if key == '3':
            hex_keys.append(0x33)
        if key == '4':
            hex_keys.append(0x34)
        if key == '5':
            hex_keys.append(0x35)
        if key == '6':
            hex_keys.append(0x36)
    if type_write:
        typewrite(text)
    else:
        print(text)
    display = ''
    while True:
        time.sleep(delay)
        for index, hex_key in enumerate(hex_keys):
            if win32api.GetKeyState(hex_key) < 0:
                display = keys[index]
                clear()
                print(text)
                print(display)
            elif win32api.GetKeyState(0x08) < 0:
                display = display[:-1]
                clear()
                print(text)
                print(display)
            elif win32api.GetKeyState(0x0D) < 0:
                return display
            
        
def color_print(text: str, color = constants.WHITE) -> None:
    """#* Prints text with color.
    """
    print(color+text)