# checkers game
# Board() -> Pawn(Board) -> Player(Pawn)
# - side choice: w / b
# - check input
# - jump after jump only from the following possible positions. If the choice of two, gives an opportunity only of them
# - queen display as a capital letter: W / B
# - queen which can go in any direction on one cell
# - can beat pawn and queen
# - bot that first beats (random from list)
# - bot jump if there is a fight after the jump
# - output of bot moves / jump
# - end game when no opponent pawns
# TODO:
# - error trapping
# - end game when no moves
# - queen go to more than one cell
# - clean code
# - bug fixes, if any

import player

while True:  # please choose a color

    player_color = input('Please select your color (w/b): ')

    if player_color.lower() in ['w', 'b']:
        break
    continue

# create an instance and display the start board
game = player.Player(player_color)
bot_color = game.get_invert(player_color)

print(game.print_board())

# start the game with the first move, depending on the user's choice
if player_color == 'w':

    while not game.win(bot_color, player_color):

        game.input(player_color)

        if not game.win(bot_color, player_color):
            game.bot(bot_color)

else:

    while not game.win(bot_color, player_color):

        game.bot(bot_color)

        if not game.win(bot_color, player_color):
            game.input(player_color)

