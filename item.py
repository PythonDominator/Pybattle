import move


class Item:
    def __init__(self, move: move.Move):
        """#* Create one use moves that characters can use in battle.
        """
        self.item = move

    def get_item(self) -> move.Move:
        return self.item