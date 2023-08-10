from pybattle.screen.colors import Color, Colors
from pybattle.screen.frames.frame import Frame
from pybattle.screen.frames.map import Map
from pybattle.screen.frames.menu import Menu, Selection, SwitchSelection, VoidSelection
from pybattle.screen.frames.weather import Rain, Weather
from pybattle.screen.grid.matrix import Cell, Matrix
from pybattle.screen.grid.point import Coord, Size
from pybattle.screen.window import Event, EventExit, EventQueue, Window, keys_pressing
from pybattle.types_ import CardinalDirection

f = Frame(Cell.from_size(Size(15, 40)))
m1 = """
╭─ BEDROOM ─┬──────────────────╮
│   ╰───────╯       ||||       │
│                   ||||       │
│                     ─┬─┬─┬─┬─┤
│                              │
│                              │
│╭│╮   ╶─╮                     │
││││    ░│                     │
│╰│╯   ╶─╯           ╭─────┬─╮ │
│                    │░░░░░│▓│ │
│                    ╰─────┴─╯ │
╰──────────────────────────────╯
"""


m2 = Map(Cell.from_str(m1), Coord(7, 22))
m2[Coord(5, 5)].value = "^"
m2[Coord(5, 5)].collision = False

f.add_frame(m2.camera())
print(f)


w = Window(f)

w.one_time_event(lambda: Rain(CardinalDirection.EAST, frequency=0.17), 3)


def update1():
    f.add_frame(m2.camera())
    w.change(f)

    # if m2[m2.pos].value == "^":
    #     w.extend_current_events(Event(lambda: EventExit.QUIT, 0.01), 3)


e1 = Event(update1, 0.01)


m2.events.append(e1)


w.run(EventQueue(m2.events))


# m = Menu(
#     Cell.from_size(Size(15, 40)),
#     [
#         SwitchSelection(
#             Selection("Start\nOver", Coord(2, 2), Colors.DEFAULT),
#             Selection("Start\nOver", Coord(2, 2), Colors.BLUE),
#         ),
#         SwitchSelection(
#             Selection("Settings", Coord(4, 6), Colors.DEFAULT),
#             Selection("Settings", Coord(4, 6), Colors.GRAY),
#         ),
#         SwitchSelection(
#             Selection("Quit", Coord(6, 2), Colors.DEFAULT),
#             Selection("Quit", Coord(6, 2), Colors.RED),
#         ),
#     ],
# )
# m2 = Menu.centered_list(
#     Cell.from_size(Size(15, 40)),
#     [
#         SwitchSelection(
#             VoidSelection("Continue", Colors.DEFAULT),
#             VoidSelection("Continue", Colors.CYAN),
#         ),
#         SwitchSelection(
#             VoidSelection("Settings", Colors.DEFAULT),
#             VoidSelection("Settings", Colors.GRAY),
#         ),
#         SwitchSelection(
#             VoidSelection("Quit", Colors.DEFAULT),
#             VoidSelection("Quit", Colors.RED),
#         ),
#     ],
# )
# #
# w = Window(m)


# def update(_):
#     w.change(m)
#     return m.switch()


# e1 = Event(update, 0.05)


# def update1(_):
#     print("hi")
#     if "BackSpace" in keys_pressing:
#         return (EventExit.BREAK_QUEUE, "Not Settings")
# def update1(_):
#     print("hi")
#     if "BackSpace" in keys_pressing:
#         return EventExit.QUIT


# e11 = Event(update1, 0.5)


# def update2(last):
#     if last["update"].label != "Settings":
#         return EventExit.BREAK

#     result = m2.switch()
#     if result is not None:
#         print("HERE", result.label)
#         w.extend_event_queue([e1])
#         return EventExit.BREAK
#     w.change(m2)


# e2 = Event(update2, 0.05)


# w.run(EventQueue([e1], [e2]))


# def update2(m, ma):
#     result = m.switch()
#     if result is not None:
#         Event(update, 0.05, ma)
#         return True
#     w.change(m)


# def update(m):
#     result = m.switch()
#     if result is not None:
#         # return result # TODO or logic here
#         m2 = Menu(
#             Cell.from_size(Size(15, 40)),
#             [
#                 SwitchSelection(
#                     Selection(result.label, Coord(2, 2), Colors.DEFAULT),
#                     Selection(result.label, Coord(2, 2), Colors.CYAN),
#                 ),
#                 SwitchSelection(
#                     Selection("Back", Coord(4, 2), Colors.DEFAULT),
#                     Selection("Back", Coord(4, 2), Colors.CYAN),
#                 ),
#             ],
#         )
#         Event(update2, 0.05, m2, m)
#         return True
#     w.change(m)
