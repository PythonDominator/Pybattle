# from pybattle.screen.frames.frame import Frame

# from pybattle.screen.grid.point import Coord, Size
# from pybattle.screen.grid.cell import Cell

# frame = Frame(Cell.from_size(Size(2, 5)))
# with open("txt.txt", "w", encoding='utf-8') as f:
#     f.write(str(frame))
import sys

sys.path.append(r"C:\Users\jacob\Downloads\Programming\Python\Pybattle\Github")
import x


frame = x.Frame(x.Cell.from_size(x.Size(2, 5)))

pyscript.write("text", str(frame))
