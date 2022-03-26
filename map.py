from email import message
import screen
import constants
import time

try:
    import win32api
except:
    pass

try:
    from pynput.keyboard import Key, Controller
except:
    pass

class Map:
    def __init__(self, map: str, location: str) -> None:
        self.map = map
        self.location = location
        self.pre = self.location
        self.values:list = self.get_values()
        self.empty_cells = self.find_empty_cells()
        self.map_cells:dict = self.get_map_cells()
        
    def find_empty_cells(self) -> list[bool]:
        empty = []
        for i in self.map:
            if i == ' ':
                empty.append(True)
            else:
                empty.append(False)
        return empty

    def get_values(self) -> list[str]:
        y = 0
        x = -1
        self.values = []
        for i in self.map:
            if i == '\n':
                y += 1
                x = -1
            else:
                x += 1
            self.values.append(f'{x}:{y}')
        return self.values
    
    def get_map_cells(self) -> dict[str: (str, bool)]:
        self.map_cells = dict(zip(self.values, zip(self.map, self.empty_cells)))
        if self.map_cells[self.location][1]:
            self.map_cells[self.location] = 'x'
            self.pre = self.location
        else:
            self.map_cells[self.pre] = 'x'
            self.location = self.pre
        return self.map_cells
    
    def get_location_cell(self) -> tuple:
        return self.get_map_cells()[self.location]
    
    def up(self) -> str:
        self.location = self.location[:self.location.find(':')]+':'+str(int(self.location[self.location.find(':')+1:])-1)
    def down(self) -> str:
        self.location = self.location[:self.location.find(':')]+':'+str(int(self.location[self.location.find(':')+1:])+1)
    def right(self) -> str:
        self.location = str(int(self.location[:self.location.find(':')])+1)+self.location[self.location.find(':'):]
    def left(self) -> str:
        self.location = str(int(self.location[:self.location.find(':')])-1)+self.location[self.location.find(':'):]
    def get_map(self) -> str:
        screen.clear()
        map = ''
        for x in self.get_map_cells():
            map += self.get_map_cells()[x][0]
        return map
    
    def loop(self, end_function, message:str='') -> None:
        x = len(self.get_map())
        print(self.get_map())
        screen.typewrite(message, clears=False)
        while True:
            if win32api.GetKeyState(0x57) < 0 or win32api.GetKeyState(0x26) < 0:
                self.up()
                print(self.get_map())
                screen.typewrite(message, 0, end_delay=0, clears=False)
                time.sleep(constants.LOOP_MAP_NUMBER / x)
            elif win32api.GetKeyState(0x41) < 0 or win32api.GetKeyState(0x25) < 0:
                self.left()
                print(self.get_map())
                screen.typewrite(message, 0, end_delay=0, clears=False)
                time.sleep(constants.LOOP_MAP_NUMBER / x)
            elif win32api.GetKeyState(0x53) < 0 or win32api.GetKeyState(0x28) < 0:
                self.down()
                screen.clear()
                print(self.get_map())
                screen.typewrite(message, 0, end_delay=0, clears=False)
                time.sleep(constants.LOOP_MAP_NUMBER / x)
            elif win32api.GetKeyState(0x44) < 0 or win32api.GetKeyState(0x27) < 0:
                self.right()
                print(self.get_map())
                screen.typewrite(message, 0, end_delay=0, clears=False)
                time.sleep(constants.LOOP_MAP_NUMBER / x)
            if end_function():
                break