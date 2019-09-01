import characters
import enemies
import random
from time import sleep


char_race = input('Your race: ')
char_name = input('Your name: ')

# Check if char_race exists
if char_race in characters.RACES:

    # Create main_char instance
    main_char = characters.RACES[char_race](char_name)

while not main_char.is_dead():

    # Randomly places for healing and monster
    hill_choice = random.choice(['u', 'd', 'l', 'r'])
    enemy_choice = random.choice(['u', 'd', 'l', 'r'])

    # call function move while the character is alive
    player_choice = main_char.move()

    if player_choice == hill_choice:

        a = main_char.hill()

    elif player_choice == enemy_choice:
        # Randomly picked enemy
        current_enemy = random.choice(enemies.ENEMIES_TYPES)()
        is_dead = main_char.on_combat(current_enemy)

    sleep(1)

        



    
    



