import move
import errors

class Weapon:
    def __init__(self, name: str, moves: list[move.Move], graphics: str, max_energy: int, damage_mult: float = 1.0) -> object:
        self.graphics = graphics
        self.name = name
        self.moves = moves
        self.max_energy = max_energy
        self.energy = self.max_energy
        self.damage_mult = damage_mult

        for index, move in enumerate(self.moves):
           if index == 0:
               self.move1 = move
           elif index == 1:
               self.move2 = move
           elif index == 2:
               self.move3 = move
           elif index == 3:
               self.move4 = move

        if len(self.get_graphics()) != 9:
           raise errors.WeaponGraphicsLengthError(f'The length of the weapon display must be 9. (Not: {len(self.get_graphics())})')
        
        if len(self.get_moves()) == 0 or len(self.get_moves()) > 4:
            raise errors.MovesLengthError(f'The length of the moves must be 1-4. (Not: {len(self.get_moves())})')
    
    def get_graphics(self) -> str:
        return self.graphics
    def get_damage_mult(self) -> float:
        return self.damage_mult
    def get_max_energy(self) -> int:
        return self.max_energy
    def get_energy(self) -> int:
        return round(self.energy)
    def get_name(self) -> str:
        return self.name
    def get_move_amount(self) -> int:
        return len(self.get_moves())
    def get_moves(self) -> list[move.Move]:
        return self.moves
    def get_move(self, index:int) -> move.Move:
        for i, x in enumerate(self.moves):
            if i == int(index)-1:
                return x
        raise errors.IndexMoveError(f'{self.get_name()} index ({index}) out of range of moves.')