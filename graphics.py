import errors
import constants

class Graphics:
    def __init__(self, hat: str, eyes: str, mouth: str, feet: str, character: object, indent: bool = False):
        """#* Create the visual for characters.
        
        #* Args:
            hat (str): Must be 7 characters long.
            eyes (str): Must be 3 characters long.
            mouth (str): Must be 1 character.
            feet (str): Must be 7 characters long.
            weapon (Weapon): The character's weapon.
            to (str): Who it is for ("target" or "player").
        
        #* Raises:
            #! GraphicsLengthError: One of the graphics is not the right length.
        """
        self.normal_eyes = eyes
        self.normal_mouth = mouth
        self.hat = hat
        self.eyes = eyes
        self.mouth = mouth
        self.feet = feet
        self.character = character
        self.indent = indent
        self.graphics = ''
                                  
        if len(self.hat) != 7:
            errors.GraphicsLengthError(f"The hat must be 7 characters long. (Not {len(self.hat)})")
        elif len(self.eyes) != 3:
            errors.GraphicsLengthError(f"The eyes must be 3 characters long. (Not {len(self.eyes)})")
        elif len(self.mouth) != 1:
            errors.GraphicsLengthError(f"The mouth must be 3 characters long. (Not {len(self.mouth)})")
        elif len(self.feet) != 7:
            errors.GraphicsLengthError(f"The feet must be 7 characters long. (Not {len(self.feet)})")
            
    def get_graphics(self) -> str:
        """#* Gets the the character's graphics with weapon and moves. Also checks for status effects for weird faces.
        """
        self.graphics = ''
        if self.character.if_confused():
            self.eyes = constants.CONFUSE_COLOR+'@ @'+constants.WHITE
            self.mouth = constants.CONFUSE_COLOR+'~'+constants.WHITE
        elif self.character.if_burned():
            self.eyes = constants.BURN_COLOR+'* *'+constants.WHITE
            self.mouth = constants.BURN_COLOR+'O'+constants.WHITE
        elif self.character.if_frozen():
            self.eyes = constants.FREEZE_COLOR+'^ ^'+constants.WHITE
            self.mouth = constants.FREEZE_COLOR+'~'+constants.WHITE
        elif self.character.if_poisoned():
            self.eyes = constants.POISON_COLOR+self.normal_eyes+constants.WHITE
            self.mouth = constants.POISON_COLOR+self.normal_mouth+constants.WHITE
        elif self.character.if_paralyzed():
            self.eyes = constants.PARALYSIS_COLOR+self.normal_eyes+constants.WHITE
            self.mouth = constants.PARALYSIS_COLOR+self.normal_mouth+constants.WHITE
        elif self.character.if_blind():
            self.eyes = '   '
            self.mouth = self.normal_mouth
        else:
            self.eyes = self.normal_eyes
            self.mouth = self.normal_mouth
            
        self.layers = ['   ' + self.hat + '   ', '   | ' + self.eyes + ' |   ', '   |  ' + self.mouth  + '  |   ', '   _|   |__  ', '__/|     | | ', '   |_____| | ', '   | | | | ^ ', '   | | | |   ', '   ' + self.feet + '   ']
        if self.character.get_items() != []:
            self.layers[self.character.weapon.get_move_amount()+2] += constants.INFO_COLOR+f'{str(self.character.weapon.get_move_amount()+2)} - View Items.'+constants.WHITE
        else:
            self.layers[self.character.weapon.get_move_amount()+2] += constants.NO_OPTION_COLOR+f'X - View Items.'+constants.WHITE
        self.layers[self.character.weapon.get_move_amount()+1] += constants.INFO_COLOR+f'{str(self.character.weapon.get_move_amount()+1)} - Rest - Gain some energy.'+constants.WHITE
        
        for i, x in enumerate(self.character.weapon.get_graphics()):
            if i > len(self.character.weapon.get_moves()) - 1:
                if self.indent:
                    self.graphics += f'\n{constants.TAB}{x}{self.layers[i]}'
                else:
                    self.graphics += f'\n{x}{self.layers[i]}'
            else:
                if self.character.weapon.get_energy() < self.character.weapon.get_moves()[i].get_energy_cost():
                    if self.indent:
                        self.graphics += f'\n{constants.TAB}{x}{self.layers[i]}{constants.NO_OPTION_COLOR}X - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()}){constants.WHITE}'
                    else:
                        self.graphics += f'\n{x}{self.layers[i]}{constants.NO_OPTION_COLOR}X - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()}){constants.WHITE}'
                else:
                    if self.character.if_paralyzed():
                        if 'health' in self.character.weapon.get_moves()[i].get_stat_type() or 'reckless' in self.character.weapon.get_moves()[i].get_stat_type():
                            if self.character.weapon.get_moves()[i].get_amount() < 0: 
                                if self.indent:
                                    self.graphics += f'\n{constants.TAB}{x}{self.layers[i]}{constants.PARALYSIS_COLOR}X - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()}){constants.WHITE}'
                                else:
                                    self.graphics += f'\n{x}{self.layers[i]}{constants.PARALYSIS_COLOR}X - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()}){constants.WHITE}'
                            else:
                                if self.indent:
                                    self.graphics += f'\n{constants.TAB}{x}{self.layers[i]}{i + 1} - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()})'
                                else:
                                    self.graphics += f'\n{x}{self.layers[i]}{i + 1} - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()})'
                        else:
                            if self.indent:
                                self.graphics += f'\n{constants.TAB}{x}{self.layers[i]}{i + 1} - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()})'
                            else:
                                self.graphics += f'\n{x}{self.layers[i]}{i + 1} - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()})'
                    else:
                        if self.indent:
                            self.graphics += f'\n{constants.TAB}{x}{self.layers[i]}{i + 1} - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()})'
                        else:
                            self.graphics += f'\n{x}{self.layers[i]}{i + 1} - {self.character.weapon.get_moves()[i].get_name()} (EC: {self.character.weapon.get_moves()[i].get_energy_cost()})'    
        return self.graphics
    def get_layers(self) -> str:
        """#* Just gets the character's graphics without their weapon and moves.
        """
        self.feet_split()
        x = ''
        for i in self.layers:
            x += i + '\n'
        return x