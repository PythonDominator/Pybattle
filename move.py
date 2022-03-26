class Move:
    def __init__(self, name: str, stat_type: str, energy_cost: int, amount: int | float = 0, extra_critical_chance: int = 0, extra_critical_power: float = 0.0):
        """#* Make some moves to use in battle.
        
        #* Args:
            disc (str): The description of the move. (Name included at the start: "Swipe - Attacks your target")
             (int | float): The percent a stat increases when you use the move OR the damage that a move does. (Depends on the stat_type)
            stat_type (Character.stat): The stat that the move boosts or decreases.
            extra_critical_chance (int, optional): The extra percent of critical chance. Defaults to 0.
            extra_critical_power (float, optional): The extra multplier of critical power. Defaults to 0.0.
        
        #* Types:
            "health": < 0: Does damage. > 0: Heals.
            "speed": < 0: Decreases target's (-float percent). > 0: Increases users (float percent).
            "attack" < 0: Decreases target's (-float percent). > 0: Increases users (float percent).
            "defense": < 0: Decreases target's (-float percent). > 0: Increases users (float percent).                                   
            "critical power" < 0: Decreases target's (-float percent). > 0: Increases user's (float percent).
            "critical chance" < 0: Decreases target's (-float percent). > 0: Increases user's (float percent).
            "dodge": If target used attacking move the attack does no damage. (no amount)
            "reckless": Does 1.5x more damage to the target but does 0.5x damage to the user. (based on -amount)
            "poison": Poisons the target. Does damage every turn until the end of the battle.
            "burn": Burns the target. Does a little damage and decreases attack. May be unburned at any turn.
            "blind": Blinds the target making them unable to do critical hits until the rest of the battle.
            "confuse": Confuses the target making them lose defense every turn. May be unconfused at any turn.
            "freeze": Freezes the target making them lose speed every turn. May be unfrozen at any turn.
            "paralyze": Paralyzes the target making them unable to attack. May be unparalyzed at any turn.
            "heal": Heals all the user's status effects.
        
        #* Prefixes:
            "may": 50% chance to do...
            "damage": Does damage and...
        """
        self.amount = amount
        self.stat_type = stat_type
        self.name = name
        self.extra_critical_chance = extra_critical_chance
        self.extra_critical_power = extra_critical_power
        self.energy_cost = energy_cost
        
    def get_amount(self) -> int | float:
        return self.amount
    def get_energy_cost(self) -> int:
        return self.energy_cost
    def get_stat_type(self) -> str:
        return self.stat_type
    def get_name(self) -> str:
        return self.name   
    def get_extra_critical_chance(self) -> int:
        return self.extra_critical_chance
    def get_extra_critical_power(self) -> float:
        return self.extra_critical_power