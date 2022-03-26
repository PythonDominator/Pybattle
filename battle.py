
import screen
import character
import constants
import random


def player_turn(player: character.Character, target: character.Character) -> bool:
    player.turn(target)
    if target.get_health() <= 0:
       screen.clear()
       screen.text(f'You won the battle.', color=constants.INCREASE_COLOR)
       return True
    elif player.get_health() <= 0:
        screen.clear()
        screen.text(f'You lost the battle.', color=constants.ERROR_COLOR)
        return True
    return False

def target_turn(player: character.Character, target: character.Character) -> bool:
    target.turn(player)
    if target.get_health() <= 0:
       screen.clear()
       screen.text(f'You won the battle.', color=constants.INCREASE_COLOR)
       return True
    elif player.get_health() <= 0:
        screen.clear()
        screen.text(f'You lost the battle.', color=constants.ERROR_COLOR)
        return True
    return False

       
def battle(player: character.Character, target: character.Character, text: str = '') -> tuple[int, bool]:
    player.total_damage_done = 0
    screen.typewrite('...')
    screen.typewrite(text)
    while True:
        screen.clear()
        
        target.reset()
        player.reset()  

        options = []
        for index, move in enumerate(player.weapon.get_moves()):
            if move.get_energy_cost() > player.weapon.get_energy():
                continue
            if player.if_paralyzed():
                if player.see('health'):
                    if move.amount() > 0: 
                        options.append(str(index+1))
                else:
                    options.append(str(index+1))        
            else:
                options.append(str(index+1))
                
        options.append(str(player.weapon.get_move_amount()+1))
        options.append(str(player.weapon.get_move_amount()+2))
            
        player.move = screen.restricted_input(
            f'{constants.TAB}{constants.NAME_COLOR}{target.get_name()}: Level: {target.get_level()}\n'
            f'{constants.TAB}{constants.ENERGY_COLOR}Energy: {target.weapon.get_energy()}/{target.weapon.get_max_energy()}\n'
            f'{constants.TAB}{constants.HEAL_COLOR}{target.get_bars()} Health: {target.get_health()}/{target.get_max_health()}{target.get_str_status_effects()}\n'
            f'{constants.TAB}{constants.WEAPON_COLOR}Weapon: {target.weapon.get_name()}\n'
            f'{constants.WHITE}{target.graphics.get_graphics()}\n'
            
            f'{constants.NAME_COLOR}{player.get_name()}: Level: {player.get_level()}\n'
            f'{constants.ENERGY_COLOR}Energy: {player.weapon.get_energy()}/{player.weapon.get_max_energy()}\n'
            f'{constants.HEAL_COLOR}{player.get_bars()} Health: {player.get_health()}/{player.get_max_health()}{player.get_str_status_effects()}\n'
            f'{constants.WEAPON_COLOR}Weapon: {player.weapon.get_name()}\n'
            f'{constants.WHITE}{player.graphics.get_graphics()}\n'
            'Press the spacebar to skip text. To zoom in and out use CTRL+scroll.\nChoose something to do: ', options)
        
        for option in options: 
            if option in player.move:
                player.move = option
                
        if str(player.weapon.get_move_amount()+2) in player.move: # TODO: Revamp
            if player.get_items() == []:
                screen.clear()
                screen.typewrite('You dont have any items.', color=constants.ERROR_COLOR)
                continue
            
            screen.clear()
            choices = []
            for i, option in enumerate(player.get_items()):
                print(f'{i+1} - {option.item.get_name()}')
                choices.append(str(i+1))

            
            player.move = input(f'Choose a item. Or to go back type "back": ')

            if player.move == 'back':
                continue
            
            for char in player.move:   
                if char in choices:
                    player.move = char
                    break
                
            if player.move in choices:
                player.used_item = True
                player.item = player.items[int(player.move) - 1]
                        
            else:
                screen.clear()
                screen.typewrite('Thats not quite right. Try something else.', color=constants.ERROR_COLOR)              
                
            
        if player.move == str(player.weapon.get_move_amount()+1):
            player.rest = True
                     
        elif not player.move in options:
            screen.clear()
            try:
                if player.weapon.get_move(player.move).get_energy_cost() > player.weapon.get_energy():
                    screen.typewrite('You don\'t have enough energy to do that move.', color=constants.ERROR_COLOR)
                else:
                    screen.typewrite('Thats not quite right. Try something else.', color=constants.ERROR_COLOR)
            except:
                screen.typewrite('Thats not quite right. Try something else.', color=constants.ERROR_COLOR)
            continue
        
        while True:
            target.move = str(random.randint(-1, target.weapon.get_move_amount()))
            
            if target.move == "0":
                if target.get_items() == []:
                    continue
                else:
                    choice = random.randint(1, len(target.get_items())) 
                    target.used_item = True
                    target.item = target.items[int(choice) - 1]
                    break
                
            if target.move == '-1':
                if target.weapon.get_energy() == target.weapon.get_max_energy():
                    continue
                else:
                    target.rest = True
                    break
            
            if ((player.if_blind() and target.see('blind')) or 
                (player.if_frozen() and target.see('freeze')) or 
                (player.if_paralyzed() and target.see('paralyze')) or 
                (player.if_confused() and target.see('confuse')) or 
                (player.if_poisoned() and target.see('poison')) or 
                (player.if_burned() and target.see('burn'))):
                continue
            
            if target.weapon.get_move(target.move).get_energy_cost() > target.weapon.get_energy():
                continue
            
            if target.if_paralyzed():
                if target.see('health') or target.see('reckless'):
                    if target.weapon.get_move(target.move).get_amount() < 0: 
                        continue
            break
        
        if player.get_speed() > target.get_speed():
            if player_turn(player, target):
                return str(player.get_total_damage_done()), True
            if target_turn(player, target): 
                return str(player.get_total_damage_done()), False

        elif player.get_speed() == target.get_speed():
            if random.randint(1, 2) == 1:
                if player_turn(player, target):
                    return str(player.get_total_damage_done()), True
                if target_turn(player, target): 
                    return str(player.get_total_damage_done()), False
            else:
                if target_turn(player, target): 
                    return str(player.get_total_damage_done()), False
                if player_turn(player, target):
                    return str(player.get_total_damage_done()), True

        else:
            if target_turn(player, target): 
                return str(player.get_total_damage_done()), False
            if player_turn(player, target):
                return str(player.get_total_damage_done()), True