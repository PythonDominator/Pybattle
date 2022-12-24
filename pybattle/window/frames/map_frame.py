from typing import Optional

from pybattle.window.frames.frame import Frame
from pybattle.window.matrix import Matrix
from pybattle.window.size import Size


class MapFrame(Frame):
    """A text map inside a Frame.
```
╭─ BEDROOM ────────────────────╮
│                   ||||       │
│                   ||||       │
│                     ─┬─┬─┬─┬─│
│                              │
│                              │
│╭│╮   ╶─╮                     │
││││    ░│                     │
│╰│╯   ╶─╯           ╭─────┬─╮ │
│                    │░░░░░│▓│ │
│                    ╰─────┴─╯ │
╰──────────────────────────────╯"""

    def __init__(
        self,
        contents: str | Matrix,
        title: Optional[str] = None,
    ) -> None:
        self.contents = Matrix(contents)
        self.size = Size(self.contents.size) + 2
        self.title = title

        self._update_frame()
