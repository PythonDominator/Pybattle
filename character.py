import weapon
import graphics
import item
import random
import constants
import errors
import move
import screen

class Character:
    def __init__(self, name: str, weapon: weapon.Weapon):
        self.name = name
        
        self.graphics:graphics.Graphics = ''
        
        self.rest = False
        
        self.paralyzed:bool = False
        self.burned:bool = False
        self.confused:bool = False
        self.blind:bool = False
        self.frozen:bool = False 
        self.poisoned:bool = False 
        self.status_effects = []

        self.item:item.Item = None
        self.items:list = []
        self.used_item:bool = False

        self.weapon:weapon.Weapon = weapon
        self.damage_done:int = 0
        self.total_damage_done:int = 0
        self.move:str = '1'
        self.critical:bool = False
        
        self.attack:int = random.randint(constants.STAT_MIN, constants.STAT_MAX)
        self.defense:int = random.randint(constants.STAT_MIN, constants.STAT_MAX)
        self.health:int = random.randint(constants.STAT_MIN, constants.STAT_MAX)
        self.speed:int = random.randint(constants.STAT_MIN, constants.STAT_MAX)

        self.critical_chance:int = constants.STARTING_CRITICAL_CHANCE
        self.critical_power:float = constants.STARTING_CRITICAL_POWER
        
        self.level:int = 0
        self.bars:str = '||||||||||||||||||||'

        self.max_attack:int = self.attack
        self.max_defense:int = self.defense
        self.max_health:int = self.health
        self.max_speed:int = self.speed

        self.max_critical_chance:int = self.critical_chance
        self.max_critical_power:float = self.critical_power

    def get_attack(self) -> int:
        return self.attack
    def get_defense(self) -> int:
        return self.defense
    def get_health(self) -> int:
        return self.health
    def get_speed(self) -> int:
        return self.speed
    def get_critical_chance(self) -> int:
        return self.critical_chance
    def get_critical_power(self) -> int:
        return self.critical_power
    
    def get_max_attack(self) -> int:
        return self.max_attack
    def get_max_defense(self) -> int:
        return self.max_defense
    def get_max_health(self) -> int:
        return self.max_health
    def get_max_speed(self) -> int:
        return self.max_speed
    def get_max_critical_chance(self) -> int:
        return self.max_critical_chance
    def get_max_critical_power(self) -> int:
        return self.max_critical_power
    
    def if_rest(self):
        return self.rest
    
    def get_bars(self) -> str:
        self.bars = round(self.get_health() / (self.get_max_health() / constants.HEALTH_BARS))
        self.bars = '|' * self.bars + '.' * (constants.HEALTH_BARS - self.bars)
        if self.bars == '....................':
            self.bars = '|...................'
        return self.bars
    def reset(self) -> None:
        """# *Resets health bars, used item, and checks to see if the character has more health than their max health and if so changes their health to their max health.
        """
        self.bars = self.get_bars()
        self.used_item = False
        self.rest = False
        if self.health > self.max_health:
            self.health = self.max_health
        if self.weapon.get_energy() > self.weapon.get_max_energy():
            self.weapon.energy = self.weapon.get_max_energy()
    def get_level(self) -> int:
        """#* Takes sum the stats divided by the LEVEL_DIVIDER. It times the critical chance and critical power to make the normal amount equal stat avg so each stat is EQUALLY IMPORTANT.
        """
        stat_avg = (constants.STAT_MIN + constants.STAT_MAX) / 2
        self.level:int = ((self.max_attack + 
                          self.max_defense + 
                          self.max_health + 
                          self.max_speed +
                          (self.max_critical_power * stat_avg / self.max_critical_power) +
                          (self.max_critical_chance * stat_avg / self.max_critical_chance))
                          # Igorne this bug, this is code.
                          // constants.LEVEL_DIVIDER)
        return int(self.level)
    
    
    
    
    # *CRITS
    def get_crit(self) -> int:
        """#* Get the critical power if a move lands on a critical hit. Otherwise it returns 1.
        """
        # Uniform makes it a decimal for more accurate measures.
        number = random.uniform(0, 100 / (self.get_critical_chance() + self.weapon.get_move(self.get_move()).get_extra_critical_chance()))
        if number < 1:
            self.critical = True
            return self.get_critical_power() + self.weapon.get_move(self.get_move()).get_extra_critical_power()
        else:
            self.critical = False
            return 1

    # *ITEMS
    def get_items(self) -> list[item.Item]:
        return self.items
    def if_used_item(self) -> bool:
        return self.used_item
    def get_item(self) -> item.Item:
        return self.item.get_item()
    def use_item(self, target: object):
        """#* Uses a item then removes it.
        """
        if self.get_items() != []:
            self.damage_done = 0
            target.damage_done = 0
            
            def see(stat_type):
                if stat_type in self.get_item().stat_type:
                    return True
                else:
                    return False
        
            def play():
                # *BASIC BUFFS
                if see("health"):
                    if self.get_item().get_amount() > 0:
                        healed = round(self.max_health * self.get_item().get_amount())
                        self.health += healed
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and healed {healed} damage.', color=constants.HEAL_COLOR)
                    elif self.get_item().get_amount() < 0:
                        self.damage_done = -(self.get_item().get_amount() * self.get_attack_mult(target))
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and it did {self.get_damage_done()} damage.', color=constants.DAMAGE_COLOR)
                            
                elif see("speed"):
                    if self.get_item().get_amount() > 0:
                        self.speed += self.speed * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and increased its speed by {str(self.get_item().get_amount())[2:]}.', color=constants.INCREASE_COLOR)
                    elif self.get_item().get_amount() < 0:
                        target.speed += target.speed * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and decreased {target.get_name()}\'s speed by {str(self.get_item().get_amount())[3:]}.', color=constants.DECREASE_COLOR)
                    
                elif see("attack"):
                    if self.get_item().get_amount() > 0:
                        self.attack += self.attack * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and increased its attack by {str(self.get_item().get_amount())[2:]}.', color=constants.INCREASE_COLOR)
                    elif self.get_item().get_amount() < 0:
                        target.attack += target.attack * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and decreased {target.get_name()}\'s attack by {str(self.get_item().get_amount())[3:]}.', color=constants.DECREASE_COLOR)
                        
                elif see("defense"):
                    if self.get_item().get_amount() > 0:
                        self.defense += self.defense * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and increased its defense by {str(self.get_item().get_amount())[2:]}.', color=constants.INCREASE_COLOR)
                    elif self.get_item().get_amount() < 0:
                        target.defense += target.defense * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and decreased {target.get_name()}\'s defense by {str(self.get_item().get_amount())[3:]}.', color=constants.DECREASE_COLOR)
                        
                elif see("critical power"):
                    if self.get_item().get_amount() > 0:
                        self.critical_power += self.critical_power * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and increased its critical power by {str(self.get_item().get_amount())[2:]}.', color=constants.INCREASE_COLOR)
                    elif self.get_item().get_amount() < 0:
                        target.critical_power += target.critical_power * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and decreased {target.get_name()}\'s critical power by {str(self.get_item().get_amount())[3:]}.', color=screen.colorama.Fore.LIGHTRED_EX)
                        
                elif see("critical chance"):
                    if self.get_item().get_amount() > 0:
                        self.critical_chance += self.critical_chance * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and increased its critical chance by {str(self.get_item().get_amount())[2:]}.', color=constants.INCREASE_COLOR)
                    elif self.get_item().get_amount() < 0:
                        target.critical_chance += target.critical_chance * self.weapon.get_move(self.get_move()).get_amount()
                        screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and decreased {target.get_name()}\'s critical chance by {str(self.get_item().get_amount())[3:]}.', color=constants.DECREASE_COLOR)
                
                elif see("dodge"):
                    if self.if_dodged():
                        if not target.get_used_item() and see("health") and self.get_item().get_amount() < 0:
                            self.health += target.get_damage_done()
                            screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and dodged {target.get_name()}\'s attack.', color=constants.DODGE_COLOR)
                        else:
                            screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} but the dodge failed.', color=constants.MISS_COLOR)
                
                # *STATUS EFFECTS
                elif see("poison"):
                    target.poisoned = True
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and poisoned {target.get_name()}.', color=constants.POISON_COLOR)
                elif see("burn"):
                    target.burned = True
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and burned {target.get_name()}.', color=constants.BURN_COLOR)
                elif see("blind"):
                    target.blind = True
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and blind {target.get_name()} ({target.get_name()} can not do critical hits).', color=constants.BLIND_COLOR)
                elif see("confuse"):
                    target.confused = True
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and confused {target.get_name()}.', color=constants.CONFUSE_COLOR)
                elif see("freeze"):
                    target.frozen = True
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and froze {target.get_name()}.', color=constants.FREEZE_COLOR)
                elif see("paralyze"):
                    target.paralyzed = True
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and paralyzed {target.get_name()}.', color=constants.PARALYSIS_COLOR)
                elif see("heal"):
                    self.poisoned = False
                    self.paralyzed = False
                    self.burned = False
                    self.frozen = False
                    self.blind = False
                    self.confused = False
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and they healed all their status effects.', color=constants.INCREASE_COLOR)
                
                target.health -= self.get_damage_done()
                self.health -= target.get_damage_done()
                self.total_damage_done += self.get_damage_done()       
            
            # *KEYWORDS
            if see("may"):
                if random.randint(1, 2) == 1:
                    play()
                else:
                    screen.typewrite(f'{self.get_name()} used a {self.get_item().get_name()} and it missed.', color=constants.MISS_COLOR)
                    
            elif see("damage"):
                self.damage_done = -(self.get_item().get_amount() * self.get_attack_mult(target) * self.get_crit())
                play()
                screen.typewrite(f'{self.get_name()}\'s {self.get_item().get_name()} also did {self.get_damage_done()} damage to {target.get_name()}.', color=constants.DAMAGE_COLOR)
            else:
                play()
            
            self.remove_item(self.item)
        
        else:
            return errors.NoItemError(f'{self.get_name()} has no items.')
    def remove_item(self, item):
        self.items.remove(item)
    def add_item(self, item):
        self.items.append(item)

    def create_graphics(self, graphics):
        self.graphics = graphics
    def get_name(self) -> str:
        return self.name
    
    def get_damage_done(self) -> int:
        return round(self.damage_done)
    def get_attack_mult(self, target:object) -> float:
        """#* Get the attack multiplier. (character's attack / target's defense)
        """
        return self.get_attack() / target.get_defense()
    def create_weapon(self, weapon):
        self.weapon = weapon
    def get_total_damage_done(self) -> int:
         return round(self.total_damage_done)
    
    def if_dodged(self) -> bool:
        return self.dodged
    def if_poisoned(self) -> bool:
        return self.poisoned
    def if_paralyzed(self) -> bool:
        return self.paralyzed
    def if_burned(self) -> bool:
        return self.burned
    def if_confused(self) -> bool:
        return self.confused
    def if_blind(self) -> bool:
        return self.blind
    def if_frozen(self) -> bool:
        return self.frozen
    def get_status_effects(self) -> list:
        return self.status_effects
    def status_effect_shorten(self, effect:bool, shorten:str) -> None:
        """#* Adds shortened status effects to the status effects.

        #* Args:
            effect (bool): If the effect is True it add the shortened status effect to the status effects. If it is False it will remove the shortened status effect from the status effects.
            shorten (str): The shorten version to add to the status effects.
        """
        if effect:
            if ' ' + shorten not in self.status_effects:
                self.status_effects.append(' ' + shorten)
        else:
            if ' ' + shorten in self.status_effects:
                self.status_effects.remove(' ' + shorten)
    def get_str_status_effects(self) -> str:
        """#* Gets the shortened status effects.
        """
        self.status_effect_shorten(self.if_poisoned(), constants.POISON_COLOR+'PSN')
        self.status_effect_shorten(self.if_burned(), constants.BURN_COLOR+'BRN')
        self.status_effect_shorten(self.if_paralyzed(), constants.PARALYSIS_COLOR+'PAR')
        self.status_effect_shorten(self.if_blind(), constants.BLIND_COLOR+'BLD')
        self.status_effect_shorten(self.if_confused(), constants.CONFUSE_COLOR+'CON')
        self.status_effect_shorten(self.if_frozen(), constants.FREEZE_COLOR+'FRZ')
        result = ''
        for status_effect in self.get_status_effects():   
            result += status_effect
        return result
    
    def add_move(self, move:move.Move):
        """#* Adds a move to the character.

        #* Raises:
            #! MovesLengthError: There is too many or not enough moves. (It must be 1-4 moves)
        """
        self.moves += move
        if len(self.get_moves()) > 4:
            raise errors.MovesLengthError(f'The length of the moves must be 1-4. (Not: {len(self.get_moves())})')
    def remove_move(self, move:move.Move):
        """#* Removes a move from the character.

        #* Raises:
            #! MovesLengthError: There is too many or not enough moves. (It must be 1-4 moves)
        """
        self.moves.remove(move)
        if len(self.get_moves()) < 1:
            raise errors.MovesLengthError(f'The length of the moves must be 1-4. (Not: {len(self.get_moves())})')
    def get_move(self) -> int:
        return self.move
    
    def see(self, stat_type):
        if stat_type in self.weapon.get_move(self.get_move()).get_stat_type():
            return True
        else:
            return False
            
    def use_move(self, target: object):
        """#* Does the character's move.
        """
        self.damage_done = 0
        target.damage_done = 0
        
        def play():
            percent = (str(self.weapon.get_move(self.get_move()).get_amount())+'0')[2:]
            if int(percent) > 100:
                percent = percent[:-1]
            if self.see("health"):
                if self.weapon.get_move(self.get_move()).get_amount() > 0:
                    healed = round(self.max_health * self.weapon.get_move(self.get_move()).get_amount())
                    self.health += healed
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and healed {healed} damage.', color=constants.HEAL_COLOR)
                elif self.weapon.get_move(self.get_move()).get_amount() < 0:
                    self.damage_done = -(self.weapon.get_move(self.get_move()).get_amount() * self.get_attack_mult(target) * self.get_crit() * self.weapon.get_damage_mult())
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and it did {self.get_damage_done()} damage.', color=constants.DAMAGE_COLOR)
                    if self.critical:
                        screen.typewrite(f'{self.get_name()} got a critical hit.', color=constants.CRITICAL_COLOR)
                    if self.paralyzed:
                        target.health += self.get_damage_done()
                        screen.typewrite(f'But {self.get_name()} is paralyzed and can not do any damage.', color=constants.PARALYSIS_COLOR)
            elif self.see("speed"):
                if self.weapon.get_move(self.get_move()).get_amount() > 0:
                    self.speed += self.speed * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and increased its speed by {percent}%.', color=constants.INCREASE_COLOR)
                elif self.weapon.get_move(self.get_move()).get_amount() < 0:
                    target.speed += target.speed * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and decreased {target.get_name()}\'s speed by {percent}%.', color=constants.DECREASE_COLOR)
            elif self.see("attack"):
                if self.weapon.get_move(self.get_move()).get_amount() > 0:
                    self.attack += self.attack * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and increased its attack by {percent}%.', color=constants.INCREASE_COLOR)
                elif self.weapon.get_move(self.get_move()).get_amount() < 0:
                    target.attack += target.attack * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and decreased {target.get_name()}\'s attack by {percent}%.', color=constants.DECREASE_COLOR)
            elif self.see("defense"):
                if self.weapon.get_move(self.get_move()).get_amount() > 0:
                    self.defense += self.defense * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and increased its defense by {percent}%.', color=constants.INCREASE_COLOR)
                elif self.weapon.get_move(self.get_move()).get_amount() < 0:
                    target.defense += target.defense * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and decreased {target.get_name()}\'s defense by {percent}%.', color=constants.DECREASE_COLOR)
            elif self.see("critical power"):
                if self.weapon.get_move(self.get_move()).get_amount() > 0:
                    self.critical_power += self.critical_power * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and increased its critical power by {percent}%.', color=constants.INCREASE_COLOR)
                elif self.weapon.get_move(self.get_move()).get_amount() < 0:
                    target.critical_power += target.critical_power * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and decreased {target.get_name()}\'s critical power by {percent}%.', color=constants.DECREASE_COLOR)
            elif self.see("critical chance"):
                if self.weapon.get_move(self.get_move()).get_amount() > 0:
                    self.critical_chance += self.critical_chance * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and increased its critical chance by {percent}%.', color=constants.INCREASE_COLOR)
                elif self.weapon.get_move(self.get_move()).get_amount() < 0:
                    target.critical_chance += target.critical_chance * self.weapon.get_move(self.get_move()).get_amount()
                    screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and decreased {target.get_name()}\'s critical chance by {percent}%.', color=constants.DECREASE_COLOR)
            
            elif self.see("dodge"):
                if self.if_dodged(): # Dodge
                    if not target.get_used_item() and self.see("health") and self.weapon.get_move(self.get_move()).get_amount() < 0: # If target used a attacking move
                        self.health += target.get_damage_done()
                        screen.typewrite(f'{self.get_name()} dodged {target.get_name()}\'s attack.', color=constants.DODGE_COLOR)
                    else:
                        screen.typewrite(f'{self.get_name()}\'s dodge failed.', constants.MISS_COLOR)
            
            elif self.see("reckless") and self.move != '5':
                self.damage_done = -(self.weapon.get_move(self.get_move()).get_amount() * 1.5 * self.get_attack_mult(target) * self.get_crit())
                target.damage_done = -(self.weapon.get_move(self.get_move()).get_amount() * 0.5 * self.get_attack_mult(self))
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and it did {self.get_damage_done()} damage.', color=constants.DAMAGE_COLOR)
                screen.typewrite(f'But {self.get_name()} did {target.get_damage_done()} damage to itself.', color=constants.DAMAGE_COLOR)
                
            elif self.see("poison"):
                target.poisoned = True
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and poisoned {target.get_name()}.', color=constants.POISON_COLOR)
            elif self.see("burn"):
                target.burned = True
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and burned {target.get_name()}.', color=constants.BURN_COLOR)
            elif self.see("blind"):
                target.blind = True
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and blind {target.get_name()} ({target.get_name()} can not do critical hits).', color=constants.BLIND_COLOR)
            elif self.see("confuse"):
                target.confused = True
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and confused {target.get_name()}.', color=constants.CONFUSE_COLOR)
            elif self.see("freeze"):
                target.frozen = True
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and froze {target.get_name()}.', color=constants.FREEZE_COLOR)
            elif self.see("paralyze"):
                target.paralyzed = True
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and paralyzed {target.get_name()}.', color=constants.PARALYSIS_COLOR)
            elif self.see("heal"):
                self.poisoned = False
                self.paralyzed = False
                self.burned = False
                self.frozen = False
                self.blind = False
                self.confused = False
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_moves(self.get_move()).get_name()} and they healed all their status effects.', color=constants.INCREASE_COLOR)
                
            else:
                raise ValueError('ERROR')
            
            target.health -= self.get_damage_done()
            self.health -= target.get_damage_done()   
            self.total_damage_done += self.get_damage_done()       
        
        if self.see("may"):
            if random.randint(1, 2) == 1:
                play()
            else:
                screen.typewrite(f'{self.get_name()} used {self.weapon.get_move(self.get_move()).get_name()} and it missed.', color=constants.MISS_COLOR)
                
        elif self.see("damage"):
            self.damage_done = -(self.weapon.get_move(self.get_move()).get_amount() * self.get_attack_mult(target) * self.get_crit())
            play()
            screen.typewrite(f'{self.get_name()}\'s {self.weapon.get_move(self.get_move()).get_name()} also did {self.get_damage_done()} damage to {target.get_name()}.', color=constants.DAMAGE_COLOR)
        else:
            play()
            
        self.weapon.energy -= self.weapon.get_move(self.get_move()).get_energy_cost()

    def turn(self, target: object):
        """#* Texts out what happenend the character's their turn.
        """
        screen.clear()
        if self.if_used_item():
            self.use_item(target)
        elif self.if_rest():
            self.weapon.energy += self.weapon.get_max_energy() * constants.REST_ENERGY
            screen.typewrite(f'{self.get_name()} rested and gained some energy.')
        else:
            self.use_move(target)
        
        if self.if_poisoned():
            target.damage_done = self.max_health * constants.POISON_DAMAGE_PERCENT * target.get_attack_mult(target)
            self.health -= target.get_damage_done()
            target.total_damage_done += target.get_damage_done()
            screen.typewrite(f'{self.get_name()} is poisoned and it did {target.get_damage_done()} damage.', color=constants.POISON_COLOR)
            target.damage_done = 0
                    
        if self.if_paralyzed():
            if random.randint(1, constants.PARALYSIS_CHANCE) == 1:
                screen.typewrite(f'{self.get_name()} is unparalyzed.', color=constants.PARALYSIS_COLOR)
                self.paralyzed = False
        
        if self.if_burned():
            target.damage_done = self.max_health * constants.BURN_HEALTH_PERCENT * target.get_attack_mult(target) # Damage
            self.health -= target.get_damage_done()
            target.total_damage_done += target.get_damage_done()
            screen.typewrite(f'{self.get_name()} is burned and it did {target.get_damage_done()} damage.', color=constants.BURN_COLOR)
            target.damage_done = 0
            self.attack -= self.attack * constants.BURN_ATTACK_PERCENT # Attack
            if str(constants.BURN_ATTACK_PERCENT)[-1] != '5': # !0.30 would round to 0.3 and it would say 3% instead of 30%
                screen.typewrite(f'{self.get_name()} also lost {str(constants.BURN_ATTACK_PERCENT)[2:3]}0% of its attack due to being burned.', color=constants.BURN_COLOR)
            else:
                screen.typewrite(f'{self.get_name()} also lost {str(constants.BURN_ATTACK_PERCENT)[2:4]}% of its attack due to being burned.', color=constants.BURN_COLOR)
            if random.randint(1, constants.BURN_CHANCE) == 1:
                screen.typewrite(f'{self.get_name()} is unburned.', color=constants.BURN_COLOR)
                self.burned = False
        
        if self.if_confused():
            self.defense -= self.defense * constants.CONFUSE_DEFENSE_PERCENT # Defense
            if str(constants.CONFUSE_DEFENSE_PERCENT)[-1] != '5': # !0.30 would round to 0.3 and it would say 3% instead of 30%
                screen.typewrite(f'{self.get_name()} is confused and lost {str(constants.CONFUSE_DEFENSE_PERCENT)[2:3]}0% of its defense.', color=constants.CONFUSE_COLOR)
            else:
                screen.typewrite(f'{self.get_name()} is confused and lost {str(constants.CONFUSE_DEFENSE_PERCENT)[2:4]}% of its defense.', color=constants.CONFUSE_COLOR)
            if random.randint(1, constants.CONFUSE_CHANCE) == 1:
                screen.typewrite(f'{self.get_name()} is unconfused.', color=constants.CONFUSE_COLOR)
                self.confused = False
        
        if self.if_frozen():
            self.speed -= self.speed * constants.FREEZE_SPEED_PERCENT # Speed
            if str(constants.FREEZE_SPEED_PERCENT)[-1] != '5': # !0.30 would round to 0.3 and it would say 3% instead of 30%
                screen.typewrite(f'{self.get_name()} is frozen and lost {str(constants.FREEZE_SPEED_PERCENT)[2:3]}0% of its speed.', color=constants.FREEZE_COLOR)
            else:
                screen.typewrite(f'{self.get_name()} is frozen and lost {str(constants.FREEZE_SPEED_PERCENT)[2:4]}% of its speed.', color=constants.FREEZE_COLOR)
            if random.randint(1, constants.FREEZE_CHANCE) == 1:
                screen.typewrite(f'{self.get_name()} is unfrozen.', color=constants.FREEZE_COLOR)
                self.frozen = False