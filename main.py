
import random
import time
import battle
import character
import item
import move
import weapon
import screen
import graphics
import map
import constants
import playsound 

# TODO: GitHub
# TODO: Name

print('Use ctrl+scroll to zoom in this far ------------------------------------------------------------------------>')
input('Press enter when your ready... ')

screen.clear()

#                  11 14 17 20 23 26 29 32 35
#                 10 13 16 19 22 25 28 31 34 37
#       0123456789  12 15 18 21 24 27 30 33 36
print(f'BREAKING NEWS!_______________________\n'#0
        '|                                    |\n'#1
        '|             ///|||\\\\\              |\n'#2
        '|           ////     \\\\\\\            |\n'#3
        '|          ///  ,   ,  \\\\\           |\n'#4
        '|         /\ |    -    | /\          |\n'#5
        '|         /\  \_     _/  /\          |\n'#6
        '|         /\  __|    |__ /\          |\n'#7
        '|         ___/          \___         |\n'#8
        '|        /                  \        |\n'#9
        '______________________________________\n')#10

screen.typewrite('Newsreporter: This just in! The smallest snow storm ever has appeared on a grave in southeast Leyen. '
             'Meteorologists are stumped by this abnormality in the weather that appeared in such a small place. '
             'As we continue to investigate, we will keep you informed. '
             'As always, tune into Leyen News on 6 to stay up to date with everything happening. ')

hair = '_-----_'
mouth = '-'
eyes = ', ,'
feet = '|_| |_|'

def dresser():
    hairs = ('_-----_', '_-|||-_', '_-===-_', '_-///-_')
    hair_num = 1
    eyes = ('. .', ', ,', '* *', '- -', '_ _', '^ ^', "' '")
    eyes_num = 1
    mouths = ('-', '>', '~', '`', 'o')
    mouths_num = 1
    feet = ('|_| |_|', '\_| |_/', '/_| |_\\', '\_/ \_/', '/_\ /_\\')
    feet_num = 1
    while True:
        screen.clear()
        change = screen.restricted_input('Change your character:\n'
            f'1 - Hair ({hair_num}): {hairs[hair_num-1]}\n'
            f"2 - Eyes ({eyes_num}): | {eyes[eyes_num-1]} |\n"
            f"3 - Mouth ({mouths_num}):|  {mouths[mouths_num-1]}  |\n"
            f"              _|   |__\n"
           f"           __/|     | |\n"
            f"              |_____| |\n"
            f"              | | | | ^\n"
            f"              | | | |  \n"
            f"4 - Feet ({feet_num}): {feet[feet_num-1]}\n"
           f'5 - Done\n'
           'Select 1, 2, 3, 4, or 5. ', ['1', '2', '3', '4', '5'])
        if change == '1':
          if hair_num >= len(hairs):
                hair_num = 1
          else:
                hair_num += 1
        elif change == '2':
            if eyes_num >= len(eyes):
                eyes_num = 1
            else:
                eyes_num += 1
        elif change == '3':
            if mouths_num >= len(mouths):
                mouths_num = 1
            else:
                mouths_num += 1
        elif change == '4':
            if feet_num >= len(feet):
                 feet_num = 1
            else:
                 feet_num += 1
        elif change == '5':
            hair = hairs[hair_num-1]
            eyes = eyes[eyes_num-1]
            mouth = mouths[mouths_num-1]
            feet = feet[feet_num-1]
            break
                  
          
#                           11 14 17 20 23 26 29
#                          10 13 16 19 22 25 28 32
#                0123456789  12 15 18 21 24 27 30
home_bedroom = ('BEDROOM_________________________\n'#0
                '|   |DRESSER|        ||||      |\n'#1
                '|                    ||||______|\n'#2
                '|                        ======|\n'#3
                '|                              |\n'#4
                '|                              |\n'#5
                '| |                            |\n'#6
                '| |  |||                       |\n'#7
                '| |                            |\n'#8
                '|                ||  (||||||[] |\n'#9
               '|                ||  (||||||[] |\n'#10
                '________________________________\n')
home_bedroom = map.Map(home_bedroom, '4:7')
def func():
    if home_bedroom.location == '20:1' or home_bedroom.location == '20:2':
        return True
    elif home_bedroom.location == '6:2' or home_bedroom.location == '7:2' or home_bedroom.location == '8:2' or home_bedroom.location == '9:2' or home_bedroom.location == '10:2':
        dresser()
        home_bedroom.down()
        print(home_bedroom.get_map())
    return False

home_bedroom.loop(func, 'Hey honey, could you please come downstairs?')

#                   11 14 17 20 23 26 29 32
#                  10 13 16 19 22 25 28 31
#        0123456789  12 15 18 21 24 27 30
home_map = ('HOME____________________________\n'#0
        '|  _____  | []             |    |\n'#1
        '|  |   |  | []             |____|\n'#2
        '|  |   |__| []             |====|\n'#3
        '|__|                       |====|\n'#4
        '|      X                        |\n'#5
        '|                               |\n'#6
        '                      () ____   |\n'#7
        '|                        [==]   |\n'#8
        '|     __              [|      | |\n'#9
        '| [= |__| =]          [|  ()  | |\n'#10
        '|                     [|      | |\n'#11
        '_________________________________\n')#12
home = map.Map(home_map, '28:5')
print(home.get_map())
for i in range(18):
    time.sleep(constants.LOOP_MAP_NUMBER / len(home_map))
    home.left()
    print(home.get_map())
    screen.typewrite('Mom: Oh, there you are. Your father called a moment ago. '
            'He was at the grave when the snow storm came. '
            'He said something very interesting has happened to grandpa\'s grave. '
           'He insists on showing you. '
             'Oh, before you go I want to give you a Pywatch. I will let you set it up. ')
while True:
    screen.clear()
    name = input(f'PYWATCH_______________________________\n'
                   '|                                    |\n'
                   '|              Welcome               |\n'
                   '|          Enter your name           |\n'
                   '|          _______________           |\n'
                   '______________________________________\n')
   
    new_name = ''
    for char in name:
        if char != ' ':
            new_name += char
    name = new_name.capitalize()
   
    if len(name) > 8:
        screen.text('Thats too long. Try again.', constants.ERROR_COLOR)
    if len(name) <= 3:
        screen.text('Thats too short. Try again.', constants.ERROR_COLOR)
       
    screen.clear()
    choice = input(f'PYWATCH_______________________________\n'
                     '|                                    |\n'
                     '|          Is this correct?          |\n'
                    f'|              {name}{" " * (22 - len(name))}|\n'
                    f'|             Yes / No               |\n'
                     '______________________________________\n')
   
    if choice.lower() == 'yes':
         break

screen.clear()
ID = random.randint(1000, 9999)
print(f'LEYEN ID_____________________________\n'
        '|    _____    |                      |\n'
        '|   /_/_\_\   |                      |\n'
        '|  |__|_|__|  |                      |\n'
        '|   \_\_/_/   |                      |\n'
        '|_____________|                      |\n'
        '|                                    |\n'
       f'|   ID: {ID}       Name: {name}{" " * (12 - len(name))}|\n'
        '|                                    |\n'
        '|   Pycoins: 0     City: Leyen       |\n'
        '______________________________________\n')
time.sleep(5)
print(home.get_map())
def func():
    if home.location == '0:7':
        return True
    return False
home.loop(func, 'Mom: I will teach you more about your new PyWatch later. '
                 'Don\'t forget your father wanted you to go see him at the graveyard.')
def home_room():
    def func():
        if home_bedroom.location == '20:1' or home_bedroom.location == '20:2':
            home.location = '27:5'
            home_mom()
            return True
        return False
    home_bedroom.loop(func)

def home_mom():
    print(home.get_map())
    def func():
        if home.location == '0:7':
            return True
        if home.location == '28:5' or home.location == '29:5' or home.location == '30:5' or home.location == '31:5':
            home_bedroom.location = '18:2'
            home_room()
            return True
        return False
    home.loop(func)
#                    11 14 17 20 23 26 29 33 36 39 42 45 48
#                   10 13 16 19 22 25 28 32 35 38 41 44 47 50
#         0123456789  12 15 18 21 24 27 30 34 37 40 43 46 49
leyen = ('LENYEN___________________________________________\n'#0
          '|                            |              /\  |\n'#1
          '|                            |   /\  ^          |\n'#2
          '|                                        ^      |\n'#3
          '|                            |   ^          /\  |\n'#4
          '|                            |____GRAVEYARD_____|\n'#5
          '|                                            ___|\n'#6
          '|                                          _/    \n'#7
          '|                                         /      \n'#8
          '|                                        /    _/|\n'#9
          '|    ___HOME___                         |    /  |\n'#10
          '|  _=============_                    =ROUTE1=  |\n'#11
          '|  | [+] ___ [+] |                     ||||||   |\n'#12
          '|  |_____| |_____|                    ========  |\n'#13
          '|                                      |    |   |\n'#14
          '________________________________________\    \____\n')#15

leyen = map.Map(leyen, '10:14')
def func():
    if leyen.location == '30:3':
        return True
    if leyen.location == '10:13':
        home.location = '1:7'
        home_mom()
        leyen.location = '10:14'
    return False
leyen.loop(func)
#                                  11 14 17 20 23 26 29 33 36
#                                 10 13 16 19 22 25 28 32 35
#                       0123456789  12 15 18 21 24 27 30 34 37
graveyard_map_snow = (f'GRAVEYARD____________________________\n'#0
                        '|      __                    /\     |\n'#1
                        '|     /  \                          |\n'#2
                        '|    |__ _|                         |\n'#3
                        '|                          __       |\n'#4
                        '|                /\       (  )      |\n'#5
                        '                         (____)     |\n'#6
                        '|                         .. .      |\n'#7
                        '|                     X  . __..     |\n'#8
                        '|       /\               ./  \ .    |\n'#9
                        '|                      . |_ __|.    |\n'#10
                        '|                                   |\n'#11
                        '_____________________________________\n')#12


graveyard = map.Map(graveyard_map_snow, '1:6')
print(graveyard.get_map())
for i in range(21):
    time.sleep(constants.LOOP_MAP_NUMBER / len(graveyard_map_snow))
    graveyard.right()
    print(graveyard.get_map())
screen.typewrite(f'Dad: Oh, there you are, {name}! I see you got the message from your mother. '
              'You’ll never believe what just happened. '
              'First, I was outside when I saw a snow storm over grandpa\'s grave. Snow was drifting down so quickly in a small spot. '
              'I brushed off the snow from grandpa’s grave. '
              'That’s when the text on the grave unexpectedly began to glow and the letters completely rearranged themselves! ')
# #                                 11 14 17 20 23 26 29 33 36
 #                                10 13 16 19 22 25 28 32 35
 #                      0123456789  12 15 18 21 24 27 30 34 37
graveyard_map_boom = ('GRAVEYARD____________________________\n'#0
                       '|      __                    /\     |\n'#1
                       '|     /  \                          |\n'#2
                       '|    |__ _|                         |\n'#3
                       '|                                   |\n'#4
                       '|                /\                 |\n'#5
                       '                              _     |\n'#6
                       '|                         _   /\    |\n'#7
                       '|                     X  /\  ^      |\n'#8
                       '|       /\               < BOOM!__| |\n'#9
                       '|                       |_       >  |\n'#10
                       '|                                   |\n'#11
                       '_____________________________________\n')#12

graveyard = map.Map(graveyard_map_boom, '22:6')
print(graveyard.get_map())
#playsound.playsound('sound.wav')
screen.typewrite('BOOM! '
             'Dad: Wait..what’s happening now? '
             'The grave. it\'s gone. This isn’t good. The pieces seem to have all gone off in different directions. '
             'We must go and find all the pieces!', end_delay=1)
#                             11 14 17 20 23 26 29 33 36
#                            10 13 16 19 22 25 28 32 35
#                  0123456789  12 15 18 21 24 27 30 34 37
graveyard_map = (f'GRAVEYARD____________________________\n'#0
                   '|      __                    /\     |\n'#1
                   '|     /  \                          |\n'#2
                   '|    |__ _|                         |\n'#3
                   '|                                   |\n'#4
                   '|                /\                 |\n'#5
                   '                                    |\n'#6
                   '|                                   |\n'#7
                   '|                     X             |\n'#8
                   '|       /\                          |\n'#9
                   '|                                   |\n'#10
                   '|                                   |\n'#11
                   '_____________________________________\n')#12
graveyard = map.Map(graveyard_map, '22:6')
def func():
    if graveyard.location == '0:6':
        return True
    return False
graveyard.loop(func, 'That’s odd. The snow seems to have stopped. '
                     f'{name}, let\'s go back to the house to update your mother on all of this.')
#                              11 14 17 20 23 26 29 33 36
#                             10 13 16 19 22 25 28 32 35
#                  0123456789  12 15 18 21 24 27 30 34 37
graveyard_map = (f'GRAVEYARD____________________________\n'#0
                   '|      __                    /\     |\n'#1
                   '|     /  \                          |\n'#2
                   '|    |__ _|                         |\n'#3
                   '|                                   |\n'#4
                   '|                /\                 |\n'#5
                   '                                    |\n'#6
                  '|                                   |\n'#7
                  '|                                   |\n'#8
                  '|       /\                          |\n'#9
                  '|                                   |\n'#10
                  '|                                   |\n'#11
                  '_____________________________________\n')#12
graveyard = map.Map(graveyard_map, '1:6')
def graveyard_loop():
    graveyard.location = '1:6'
   
    def func():
        if graveyard.location == '0:6':
            leyen.location = '30:3'
            return True
        return False
    graveyard.loop(func)
def func():
    if leyen.location == '30:3':
        graveyard_loop()
    if leyen.location == '10:13':
        return True
    return False

leyen.loop(func)

#                   11 14 17 20 23 26 29 32
#                  10 13 16 19 22 25 28 31
#        0123456789  12 15 18 21 24 27 30
home_map = ('HOME____________________________\n'#0
        '|  _____  | []             |    |\n'#1
        '|  |   |  | []             |____|\n'#2
        '|  |   |__| []             |====|\n'#3
        '|__|                       |====|\n'#4
        '|      X  X                     |\n'#5
        '|                               |\n'#6
        '                       () ____  |\n'#7
        '|                         [==]  |\n'#8
        '|     __              [|      | |\n'#9
        '| [= |__| =]          [|  ()  | |\n'#10
        '|                     [|      | |\n'#11
        '_________________________________\n')#12

name = 'You'

home = map.Map(home_map, '1:7')
print(home.get_map())
screen.typewrite('Dad: Hey, sweetheart. I need to tell you something.\n'
            '...'
            f'Mom: {name}, we have decided to send you on a quest to retrieve the pieces. '
            'You may use your dad\'s old sword to protect you from animals in the forest. '
            'We believe you are the most capable because we are getting too old. '
            'Dad: I will teach you how to fight. Here\'s your weapon. '
            'You got an old sword from dad! ')



slash = move.Move('Slash', "health", 25, -50)
sharpen = move.Move('Sharpen', 'attack', 15, 0.25)

old_sword = weapon.Weapon('Old Sword', [slash, sharpen], '  ||-|   ', 50)

player = character.Character(name, old_sword)

x = graphics.Graphics(hair, eyes, mouth, feet, player)
player.create_graphics(x)


cut = move.Move('Cut', "health", 20, -35)
workup = move.Move('Workup', 'speed', 15, 0.25)

small_dagger = weapon.Weapon('Small Dagger', [cut, workup], '   |-|   ', 55)

dad = character.Character('Dad', small_dagger)

x = graphics.Graphics("_-----_", ', ,', '^', '|_| |_|', dad, True)
dad.create_graphics(x)

# FIX
x = battle.battle(player, dad, 'Dad: Alright, before we begin, I want to explain a few things about battling. '
                                'On your Pywatch your health is displayed in green and energy is purple. '
                                'If you run out of health you lose the battle. '
                                'In the battle, you will have four options: 1, 2, 3, 4. '
                                'On your moves 1 and 2 there will be a number next to EC. This means Energy Cost.'
                                'Each time you use a move your energy will be reduced by the Energy Cost of the move. '
                                'Once you run low on Energy, moves that you don\'t have enough energy for will be X-ed. '
                                'To regain your energy you will need to rest and enter 3. Resting will replenish some of your energy. '
                                'Option 4 will show you your items. If you don\'t have any items it will be X-ed. '
                                'Otherwise you can select one to help you. '
                                'As you progress you will get more options and moves. '
                                'Now lets begin. ')

print(home.get_map())

if x[1] == True:
    screen.typewrite('Dad: That was an excellent battle.')
screen.typewrite('I think you will do just fine finding your grandpa’s grave.')

screen.typewrite('Mom: Okay, you better get going on your adventure. We can communicate over your Pywatch. '
            'Dad: Oh, don’t forget this. Dad gave you an apple and a healing spray. '
            'Mom: Good luck!')

























































# def player_hat():
#     screen.clear()
#     while True:
#         print('Ex 1: _-----_\nEx 2: _-|||-_\nEx 3: _((*))_\n')
#         hat = screen.text('What do you want your hat/hair to be? (It must be 7 characters long) ', prompt=True)
#         if len(hat) != 7:
#             screen.text('Thats not 7 characters long.')
#         else:
#             break
#     return hat

# def player_eyes():
#     screen.clear()
#     while True:
#         print('Ex 1: . .\nEx 2: \ /\nEx 3: * *\n')
#         eyes = screen.text('What do you want your eyes to be? (It must be 3 characters long) ', prompt=True)
#         if len(eyes) != 3:
#             screen.text('Thats not 3 characters long.')
#         else:
#             break
#     return eyes

# def player_mouth():
#     screen.clear()
#     while True:
#         print('Ex 1: -\nEx 2: .\nEx 3: ^\n')
#         mouth = screen.text('What do you want your mouth to be? (It must be 1 character) ', prompt=True)
#         if len(mouth) != 1:
#             screen.text('Thats not 1 character.')
#         else:
#             break
#     return mouth

# def player_feet():
#     screen.clear()
#     while True:
#         print('Ex 1: \_| |_/\nEx 2: |__|__|\nEx 3: [__|__]\n')
#         feet = screen.text('What do you want your feet/boots to be? (It must be 7 characters long) ', prompt=True)
#         if len(feet) != 7:
#             screen.text('Thats not 7 characters long.')
#         else:
#             break
#     return feet

# def player_graphics(character):
#     hat = player_hat()
#     eyes = player_eyes()
#     mouth = player_mouth()
#     feet = player_feet()
#     while True:
#         y = graphics.Graphics(hat, eyes, mouth, feet, character)
#         print(y.get_layers())
#         x = screen.text(f'Is this want you want for your character? ', prompt=True)
#         if x.lower() != 'yes':
#             while True:
#                 print(f'Hat: {hat}\nEyes: {eyes}\nMouth: {mouth}\nFeet: {feet}\nAll\nDone\n')
#                 z = screen.text(f'What part do you want to change? ', prompt=True)
#                 if z.lower() == 'hat':
#                     hat = player_hat()
#                 elif z.lower() == 'eyes':
#                     eyes = player_eyes()
#                 elif z.lower() == 'mouth':
#                     mouth = player_mouth()
#                 elif z.lower() == 'feet':
#                     feet = player_feet()
#                 elif z.lower() == 'all':
#                     hat = player_hat()
#                     eyes = player_eyes()
#                     mouth = player_mouth()
#                     feet = player_feet()
#                 elif z.lower() == 'done':
#                     break
#                 else:
#                     screen.text('Thats not quite right. Try something else.')
#                 continue
#             continue
#         break
#     return hat, eyes, mouth, feet


# #         3  6  9  12 15 18 21 24 27 30 33 36 39 42
# #        2  5  8  11 14 17 20 23 26 29 32 35 38 41
# #       1  4  7  10 13 16 19 22 25 28 31 34 37 40
# zone = ('__________________________________________\n' # 1
#        '|                                        |\n' # 2
#        '|                                        |\n' # 3
#        '|                                        |\n' # 4
#        '|                                        |\n' # 5
#        '|                   *                    |\n' # 6
#        '|                                        |\n' # 7
#        '|                                        |\n' # 8
#        '|                                        |\n' # 9
#        '|                                        |\n' # 10
#        '|                                        |\n' # 11
#        '__________________________________________\n') # 12



# x = map.Map(zone, '2:2')

# def func():
#     if x.location == '20:6':
#         return True
#     return False

# x.loop(func)

# # TODO COMMENT
# smash = move.Move('Smash - Smack your staff on your target doing a little damage.', 'health', 10, -20)
# poison = move.Move('Poison - Poisons your target doing damage every turn for the rest of the battle.', 'poison', 30)
# paralyze = move.Move('Paralyze - Paralyzes your target making them not able to attack.', 'paralyze', 25)
# burn = move.Move('Burn - Burns your target doing some damage while decreasing their attack each turn until it runs out.', 'burn', 30)
# rainbow_effecter = weapon.Weapon('Rainbow Effecter - A magical staff that can cause many the status effects.', [smash, poison, paralyze, burn], '  *||||| ', 105)

# player = character.Character('Wizard', rainbow_effecter)
# custom = False
# if custom:
#     hat, eyes, mouth, feet = player_graphics(player)
#     wizard = graphics.Graphics(hat, eyes, mouth, feet, player, rainbow_effecter, "player")
# else:
#     wizard = graphics.Graphics('_((*))_', ', ,', '`', '/_| |_\\', player, rainbow_effecter, "player")
# player.create_graphics(wizard)

# apple = item.Item(move.Move('Apple - Heals 50% of your health.', 'health', 0, 0.50))
# player.add_item(apple)

# confuse = move.Move('Confuse - Confuses your target making them lose defense.', 'confuse', 20)
# freeze = move.Move('Freeze - Freezes your target making them slower.', 'freeze', 20)
# blind = move.Move('Blind - Blinds your target making them not able to do critical hits.', 'blind', 15)
# laser_beam = move.Move('Laser Beam - Does a lot of damage to your target.', 'reckless', 50, -40)
# magic_wand = weapon.Weapon('Magic Wand - A small stick that can cause many status effects.', [confuse, freeze, blind, laser_beam], '  *|-    ', 105)

# target = character.Character('Trickster', magic_wand)

# trickster = graphics.Graphics('_-----_', '| |', '-', '|_| |_|', target, magic_wand, 'target')
# target.create_graphics(trickster)

# target.add_item(apple)

# screen.text(battle.battle(player, target))



