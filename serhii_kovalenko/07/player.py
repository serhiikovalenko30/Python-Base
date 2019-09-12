import random
import pawn


class Player(pawn.Pawn):
    """
    Class describes player and bot
    """
    def __init__(self, color):
        """
        Init object player with his color
        """
        super().__init__()  # init board from parent class
        self.color = color

    def get_color(self):
        """
        Function return color player
        """
        return self.color

    def input(self, color='.', find_jump=[], key=0):
        """
        Function asks the user for a move and calls the parent function
        :param color: solor player
        :rtype str
        :param find_jump: list if there is a battle option
        :rtype list
        :param key: a key that indicates that there is a second battle after the move
        :rtype int
        """
        if key == 1:
            while True:
                pl_input = input(f'Please jump after jump mr."{color}". Example: a2-b3 / a2:b4 / a2 b3\n')

                if self.check_input(pl_input) and ([pl_input[3:5]]) in self.convert_jump(find_jump):

                    fr, to, color = pl_input[0:2], pl_input[3:5], color
                    self.choice_move(fr, to, color)
                    break
                continue

        elif not self.find_jump(self.SIZE, self.SIZE, color):

            while True:

                pl_input = input(f'Enter your move, mr."{color}". Example: a2-b3 / a2:b4 / a2 b3\n')

                if self.check_input(pl_input):

                    fr, to, color = pl_input[0:2], pl_input[3:5], color
                    self.choice_move(fr, to, color)
                    break
                continue

        elif self.find_jump(self.SIZE, self.SIZE, color):

            while True:

                pl_input = input(f'Please jump, mr."{color}": Example: a2-b3 / a2:b4 / a2 b3\n')

                if self.check_input(pl_input) and \
                        ([pl_input[3:5]]) in self.convert_jump(self.find_jump(self.SIZE, self.SIZE, color)):

                    fr, to, color = pl_input[0:2], pl_input[3:5], color
                    self.choice_move(fr, to, color)
                    break
                continue

    def check_input(self, inp):
        """
        Function checks user input for correctness
        :param inp: player input
        :type inp: str
        :return: lowercase string
        :rtype str
        """
        pl_input = inp

        if len(pl_input) == 5 and pl_input[0].isalpha() and pl_input[3].isalpha() and \
                pl_input[1].isdigit() and pl_input[4].isdigit() and \
                ('a' <= pl_input[0] <= 'h') and ('a' <= pl_input[3] <= 'h') and \
                (0 <= int(pl_input[1]) <= self.SIZE) and (0 <= int(pl_input[4]) <= self.SIZE):

            return pl_input.lower()

    def bot(self, color):
        """
        Function describes bot moves
        :param color: color bot pawns
        :type color: str
        :return:
        """
        if self.find_jump(self.SIZE, self.SIZE, color):  # if we can beat

            bot_jump = random.choice(self.find_jump(self.SIZE, self.SIZE, color))

            v_fr, h_fr = bot_jump[0][0][0], bot_jump[0][0][1]
            v_en, h_en = bot_jump[0][1][0], bot_jump[0][1][1]
            v_to, h_to = bot_jump[0][2][0], bot_jump[0][2][1]

            # change board
            self.board[v_to][h_to], self.board[v_fr][h_fr], self.board[v_en][h_en] = \
                color if self.get_empty(v_fr, h_fr) == color else self.get_queen(color), self.SPACE, self.SPACE

            self.set_queen(v_to, h_to, color)  # we put a queen if ok

            self.bot_output(v_fr, h_fr, v_to, h_to)

            while self.find_jump(v_to, h_to, color):  # if we can beat after beat

                add_jump = self.find_jump(v_to, h_to, color)

                v_fr, h_fr = add_jump[0][0][0][0], add_jump[0][0][0][1]
                v_en, h_en = add_jump[0][0][1][0], add_jump[0][0][1][1]
                v_to, h_to = add_jump[0][0][2][0], add_jump[0][0][2][1]

                # change board
                self.board[v_to][h_to], self.board[v_fr][h_fr], self.board[v_en][h_en] = \
                    color if self.get_empty(v_fr, h_fr) == color else self.get_queen(color), self.SPACE, self.SPACE

                self.set_queen(v_to, h_to, color)  # we put a queen if ok

                self.bot_output(v_fr, h_fr, v_to, h_to)

        else:  # if we cant beat - move

            bot_move = random.choice(self.find_move(self.SIZE, self.SIZE, color))

            v_fr, h_fr = bot_move[0][0], bot_move[0][1]
            v_to, h_to = bot_move[1][0], bot_move[1][1]

            # if queen move anywhere
            if self.get_empty(v_fr, h_fr) == self.get_queen(color):
                # change board
                self.board[v_to][h_to], self.board[v_fr][h_fr] = \
                    color if self.get_empty(v_fr, h_fr) == color else self.get_queen(color), self.SPACE

                self.bot_output(v_fr, h_fr, v_to, h_to)

            else:
                if self.get_direction(v_fr, v_to, color):
                    # change board
                    self.board[v_to][h_to], self.board[v_fr][h_fr] = \
                        color if self.get_empty(v_fr, h_fr) == color else self.get_queen(color), self.SPACE

                    self.set_queen(v_to, h_to, color)  # we put a queen if ok

                    self.bot_output(v_fr, h_fr, v_to, h_to)

                else:
                    self.bot(color)

    def bot_output(self, v_fr, h_fr, v_to, h_to):
        """
        Function collects and displays a phrase from the bot using the coordinates of the move
        :param v_fr: vertical coordinate position where come
        :type v_fr: str
        :param h_fr: horizontal coordinate position where come
        :type h_fr: str
        :param v_to: vertical coordinate position where go
        :type v_to: str
        :param h_to: horizontal coordinate position where go
        :type h_to: str
        """
        bot_text = ''
        for i in self.convert_jump([[[v_fr, h_fr], [v_to, h_to]]]):
            bot_text += ''.join(map(str, i)) + '-'

        print(f'Bot move: {bot_text[:-1]}')
        print(self.print_board())
