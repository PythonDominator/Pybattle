from __future__ import annotations

from pybattle.screen.grid.matrix import Junction
from pybattle.types_ import Direction, JunctionDict, Thickness


class BorderType:
    def __init__(
        self,
        top_right: JunctionDict,
        top_left: JunctionDict,
        bottom_right: JunctionDict,
        bottom_left: JunctionDict,
        horizontal: JunctionDict,
        vertical: JunctionDict,
    ) -> None:
        self.top_right = top_right
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.bottom_left = bottom_left
        self.horizontal = horizontal
        self.vertical = vertical

    @property
    def top_right_junction(self):
        return Junction(self.top_right)

    @property
    def top_left_junction(self):
        return Junction(self.top_left)

    @property
    def bottom_right_junction(self):
        return Junction(self.bottom_right)

    @property
    def bottom_left_junction(self):
        return Junction(self.bottom_left)

    @property
    def horizontal_junction(self):
        return Junction(self.horizontal)

    @property
    def vertical_junction(self):
        return Junction(self.vertical)

    def __repr__(self) -> str:
        return (
            f"{self.top_right_junction}{self.horizontal_junction * 4}{self.top_left_junction}\n"
            f"{self.vertical_junction}    {self.vertical_junction}\n"
            f"{self.bottom_right_junction}{self.horizontal_junction * 4}{self.bottom_left_junction}\n"
        )


def _uniform(
    thickness: Thickness,
) -> tuple[
    JunctionDict, JunctionDict, JunctionDict, JunctionDict, JunctionDict, JunctionDict
]:
    return (
        {Direction.DOWN: thickness, Direction.RIGHT: thickness},
        {Direction.DOWN: thickness, Direction.LEFT: thickness},
        {Direction.UP: thickness, Direction.RIGHT: thickness},
        {Direction.UP: thickness, Direction.LEFT: thickness},
        {Direction.LEFT: thickness, Direction.RIGHT: thickness},
        {Direction.UP: thickness, Direction.DOWN: thickness},
    )


class Borders:
    """
    ```
    Thin:
        ╭───╮
        │   │
        ╰───╯
    Thick:
        ┏━━━┓
        ┃   ┃
        ┗━━━┛
    Double:
        ╔═══╗
        ║   ║
        ╚═══╝
    """

    THIN = BorderType(*_uniform(Thickness.THIN))
    THICK = BorderType(*_uniform(Thickness.THICK))
    DOUBLE = BorderType(*_uniform(Thickness.DOUBLE))
