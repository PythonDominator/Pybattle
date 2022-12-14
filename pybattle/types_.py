from typing import TYPE_CHECKING, Union, TypeAlias

if TYPE_CHECKING:
    from pybattle.creatures.attributes.element import Element
    from pybattle.creatures.humanoid import Humanoid
    from pybattle.creatures.pymon import Pymon
    from pybattle.window.coord import Coord
    from pybattle.window.size import Size


Creature = Union["Pymon", "Humanoid"]
Attacker = Creature
Defender = Creature
User: TypeAlias = "Humanoid"

ElementReference = Union[str, "Element"]
CoordReference = Union["Coord", tuple, int]
SizeReference = Union["Size", tuple, int]