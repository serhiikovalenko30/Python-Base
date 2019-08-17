from random import randint

print('Welcome. Let\'s play at 21 with two bots.')

target = 21
one_bot_card_1 = randint(2, 11)
one_bot_card_2 = randint(2, 11)
one_bot_value = one_bot_card_1 + one_bot_card_2
two_bot_card_1 = randint(2, 11)
two_bot_card_2 = randint(2, 11)
two_bot_value = two_bot_card_1 + two_bot_card_2
player_card_1 = randint(2, 11)
player_card_2 = randint(2, 11)
player_value = player_card_1 + player_card_2

print(f'You have {player_value} points with cards {player_card_1}, {player_card_2}')
print(f'First Bot have {one_bot_value} points with cards {one_bot_card_1}, {one_bot_card_2}')
print(f'Second Bot have {two_bot_value} points with cards {two_bot_card_1}, {two_bot_card_2}')

while True:

    if player_value == target or (player_card_1 == 11 and player_card_2 == 11):

        player_value = target
        break

    if player_value > target:

        player_value = 0
        break

    player_choice = int(input('Please, enter 1 for pick card or 0 for pass:\n'))

    if player_choice:

        player_pick = randint(2, 11)
        player_value += player_pick
        print('You +', player_pick, '=', player_value)
        continue

    print('You pass')
    break

while True:

    if one_bot_value == target or (one_bot_card_1 == 11 and one_bot_card_2 == 11):

        one_bot_value = target
        break

    if one_bot_value > target:

        one_bot_value = 0
        break

    one_bot_choice = randint(0, 1)

    if one_bot_choice:

        one_bot_pick = randint(2, 11)
        one_bot_value += one_bot_pick
        print('First Bot +', one_bot_pick, '=', one_bot_value)
        continue

    print('First Bot pass')
    break

while True:

    if two_bot_value == target or (two_bot_card_1 == 11 and two_bot_card_2 == 11):

        two_bot_value = target
        break

    if two_bot_value > target:

        two_bot_value = 0
        break

    two_bot_choice = randint(0, 1)

    if two_bot_choice:

        two_bot_pick = randint(2, 11)
        two_bot_value += two_bot_pick
        print('Second bot +', two_bot_pick, '=', two_bot_value)
        continue

    print('Second Bot pass')
    break

print(f'Your score {player_value}. First Bot score {one_bot_value}. Second Bot score {two_bot_value}')

if player_value > target and one_bot_value > target and two_bot_value > target:

    print('You all lose')

elif target >= player_value > one_bot_value and target >= player_value > two_bot_value:

    print('You win')

elif target >= one_bot_value > player_value and target >= one_bot_value > two_bot_value:

    print('First Bot win')

elif target >= two_bot_value > player_value and target >= two_bot_value > one_bot_value:

    print('Second Bot win')

else:

    print('Draw')
