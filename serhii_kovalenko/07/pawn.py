import board


class Pawn(board.Board):
    """
    Class describes pawn
    """
    def get_empty(self, x, y):
        """
        Function returns the value of the cell in the board
        :param x: horizontal coordinate
        :type x: str
        :param y: vertical coordinate
        :type y: str
        :return: value cell
        :rtype: str
        """
        return self.board[x][y]

    def get_invert(self, color):
        """
        Function returns opponent color
        :param color: color player/pawn
        :type color: str
        :return: opponent color
        :rtype: str
        """
        return self.BLACK if color == self.WHITE else self.WHITE

    def get_invert_queen(self, color):
        """
        Function returns opponent queen color
        :param color: color player/pawn
        :type color: str
        :return: opponent color
        :rtype: str
        """
        return self.B_BLACK if color == self.WHITE else self.B_WHITE

    def get_direction(self, v_fr, v_to, color):
        """
        Function returns direction for player/pawn
        :param v_fr: position where come
        :type v_fr: int
        :param v_to: position where go
        :type v_to: int
        :param color: color player/pawn
        :type color: str
        :return: direction for player/pawn
        :rtype: bool
        """
        if ((v_to - v_fr) == 1 and color == self.BLACK) or ((v_to - v_fr) == -1 and color == self.WHITE):
            return True

    def get_queen(self, color):
        """
        Function returns queen value player/pawn
        :param color: color player/pawn
        :type color: str
        :return: queen value player/pawn
        :rtype: str
        """
        return self.B_BLACK if color == self.BLACK else self.B_WHITE

    def set_queen(self, x, y, color):
        """
        Function set queen if the conditions are met
        :param x: horizontal coordinate
        :type x: str
        :param y: vertical coordinate
        :type y: str
        :param color: color player/pawn
        :type color: str
        """
        if color == self.BLACK and x == 7:
            self.board[x][y] = self.get_queen(color)

        if color == self.WHITE and x == 0:
            self.board[x][y] = self.get_queen(color)

    def find_jump(self, x=8, y=8, color='.'):
        """
        Function searches for possible battle positions
        :param x: horizontal coordinate
        :type x: int
        :param y: vertical coordinate
        :type y: int
        :param color: color player/pawn
        :type color: str
        :return: list with battle positions
        :rtype: list
        """
        jump = []

        if x == 8:

            for i in self.position_on_board(color):  # iterate over every pawn

                a = self.check_jump(i[0], i[1], color)  # passes for verification
                if self.check_jump(i[0], i[1], color):
                    jump.append(a)

        if x != 8:  # if a specific pawn is transferred, then a search for it

            a = self.check_jump(x, y, color)
            if self.check_jump(x, y, color):  # passes for verification

                jump.append(a)

        return jump

    def find_move(self, x=8, y=8, color='.'):
        """
        Function searches for possible positions for move
        :param x: horizontal coordinate
        :type x: int
        :param y: vertical coordinate
        :type y: int
        :param color: color player/pawn
        :type color: str
        :return: list with battle positions
        :rtype: list
        """
        move = []

        if x == 8:

            for i in self.position_on_board(color):

                a = self.check_move(i[0], i[1], color)
                if self.check_move(i[0], i[1], color):
                    move.append(a)

        if x != 8:  # if a specific pawn is transferred, then a search for it

            a = self.check_move(x, y, color)
            if self.check_move(x, y, color):
                move.append(a)

        return move

    def check_jump(self, x, y, color):
        """
        Function to checks that all conditions are fulfilled to beat another pawn
        :param x: horizontal coordinate
        :type x: int
        :param y: vertical coordinate
        :type y: int
        :param color: color player/pawn
        :type color: str
        :return: list with end horizontal and vertical coordinate for player and all for bot
        :rtype: list
        """
        jump = []
        if ([x, y]) in self.position_on_board(color) \
                and ([x + 1, y + 1]) in self.position_on_board(self.get_invert(color)) \
                and ([x + 2, y + 2]) in self.position_on_board():

            jump.append([x + 2, y + 2] if color == self.get_color()
                        else [x + 2, y + 2] if color == self.get_queen(self.get_color())
                        else [[x, y], [x + 1, y + 1], [x + 2, y + 2]])

        if ([x, y]) in self.position_on_board(color) \
                and ([x + 1, y - 1]) in self.position_on_board(self.get_invert(color)) \
                and ([x + 2, y - 2]) in self.position_on_board():

            jump.append([x + 2, y - 2] if color == self.get_color()
                        else [x + 2, y - 2] if color == self.get_queen(self.get_color())
                        else [[x, y], [x + 1, y - 1], [x + 2, y - 2]])

        if ([x, y]) in self.position_on_board(color) \
                and ([x - 1, y - 1]) in self.position_on_board(self.get_invert(color)) \
                and ([x - 2, y - 2]) in self.position_on_board():

            jump.append([x - 2, y - 2] if color == self.get_color()
                        else [x - 2, y - 2] if color == self.get_queen(self.get_color())
                        else [[x, y], [x - 1, y - 1], [x - 2, y - 2]])

        if ([x, y]) in self.position_on_board(color) \
                and ([x - 1, y + 1]) in self.position_on_board(self.get_invert(color)) \
                and ([x - 2, y + 2]) in self.position_on_board():

            jump.append([x - 2, y + 2] if color == self.get_color()
                        else [x - 2, y + 2] if color == self.get_queen(self.get_color())
                        else [[x, y], [x - 1, y + 1], [x - 2, y + 2]])

        return jump

    def check_move(self, x, y, color):
        """
        Function to checks that all conditions are fulfilled to move another pawn
        :param x: horizontal coordinate
        :type x: int
        :param y: vertical coordinate
        :type y: int
        :param color: color player/pawn
        :type color: str
        :return: list with end horizontal and vertical coordinate for player and all for bot
        :rtype: list
        """
        if ([x, y]) in self.position_on_board(color) and ([x + 1, y + 1]) in self.position_on_board():
            return [x + 1, y + 1] if color == self.get_color() \
                else [x + 1, y + 1] if color == self.get_queen(self.get_color()) \
                else [[x, y], [x + 1, y + 1]]

        if ([x, y]) in self.position_on_board(color) and ([x + 1, y - 1]) in self.position_on_board():
            return [x + 1, y - 1] if color == self.get_color() \
                else [x + 1, y - 1] if color == self.get_queen(self.get_color()) \
                else [[x, y], [x + 1, y - 1]]

        if ([x, y]) in self.position_on_board(color) and ([x - 1, y - 1]) in self.position_on_board():
            return [x - 1, y - 1] if color == self.get_color() \
                else [x - 1, y - 1] if color == self.get_queen(self.get_color()) \
                else [[x, y], [x - 1, y - 1]]

        if ([x, y]) in self.position_on_board(color) and ([x - 1, y + 1]) in self.position_on_board():
            return [x - 1, y + 1] if color == self.get_color() \
                else [x - 1, y + 1] if color == self.get_queen(self.get_color()) \
                else [[x, y], [x - 1, y + 1]]

    def convert_jump(self, jump):
        """
        Function converts indexes list to text for bot output
        :param jump: list with coord indexes
        :type jump: list
        :return: text for output
        :rtype: list
        """
        to = []

        for i, j in enumerate(jump):
            for z in j:

                x = self.SIZE - z[0]
                y = 'a' if z[1] == 0 else 'b' if z[1] == 1 else 'c' if z[1] == 2 else 'd' \
                    if z[1] == 3 else 'e' if z[1] == 4 else 'f' if z[1] == 5 else 'g' if z[1] == 6 else 'h'

                to.append([str(y) + str(x)])

        return to

    def choice_move(self, fr, to, color='.'):
        """
        Function selects the move option (move or beat) from the transmitted data
        :param fr: horizontal coordinate
        :type fr: str
        :param to: vertical coordinate
        :type to: str
        :param color: color player/pawn
        :type color: str
        """
        v_fr, h_fr = self.Y[fr[1]], self.X[fr[0]]
        v_to, h_to = self.Y[to[1]], self.X[to[0]]
        v_en, h_en = (self.Y[to[1]] + self.Y[fr[1]]) // 2, (self.X[to[0]] + self.X[fr[0]]) // 2

        if abs(v_to - v_fr) > 1:  # if the dalt is more than one then they want to beat
            self.jump(v_fr, h_fr, v_to, h_to, v_en, h_en, color)
        else:
            self.move(v_fr, h_fr, v_to, h_to, color)

    def move(self, v_fr, h_fr, v_to, h_to, color='.'):
        """
        Function moves the pawn on the board
        :param v_fr: vertical coordinate position where come
        :type v_fr: str
        :param h_fr: horizontal coordinate position where come
        :type h_fr: str
        :param v_to: vertical coordinate position where go
        :type v_to: str
        :param h_to: horizontal coordinate position where go
        :type h_to: str
        :param color: color player/pawn
        :type color: str
        """
        # if queen, then we go in any direction
        if self.get_empty(v_fr, h_fr) == self.get_queen(color) and self.get_empty(v_to, h_to) == self.SPACE:

            self.board[v_to][h_to], self.board[v_fr][h_fr] = color if self.get_empty(v_fr, h_fr) == color \
                                                                 else self.get_queen(color), self.SPACE
            self.set_queen(v_to, h_to, color)

            print(self.print_board())

        else:

            if self.get_empty(v_fr, h_fr) == color or self.get_empty(v_fr, h_fr) == self.get_queen(color):

                if self.get_direction(v_fr, v_to, color):

                    if self.get_empty(v_to, h_to) == self.SPACE:

                        self.board[v_to][h_to], self.board[v_fr][h_fr] = color if self.get_empty(v_fr, h_fr) == color \
                                                                             else self.get_queen(color), self.SPACE
                        self.set_queen(v_to, h_to, color)  # we put a queen if ok

                        print(self.print_board())

                    else:
                        print('The cell is not empty')
                        self.input(color)

                else:
                    print(f'A pawn cannot go this way.')
                    self.input(color)

            else:
                print('Pawn is not your color')
                self.input(color)

    def jump(self, v_fr, h_fr, v_to, h_to, v_en, h_en, color='.'):
        """
        Function moves the pawn on the board
        :param v_fr: vertical coordinate position where come
        :type v_fr: str
        :param h_fr: horizontal coordinate position where come
        :type h_fr: str
        :param v_to: vertical coordinate position where go
        :type v_to: str
        :param h_to: horizontal coordinate position where go
        :type h_to: str
        :param v_en: vertical coordinate beat position
        :type v_en: str
        :param h_en: horizontal coordinate beat position
        :type h_en: str
        :param color: color player/pawn
        :type color: str
        """
        if self.get_empty(v_fr, h_fr) == color or self.get_empty(v_fr, h_fr) == self.get_queen(color):

            if self.get_empty(v_to, h_to) == self.SPACE and (self.get_empty(v_en, h_en) == self.get_invert(color) or
                                                             self.get_empty(v_en, h_en) == self.get_invert_queen(color)):

                self.board[v_to][h_to], self.board[v_fr][h_fr], self.board[v_en][h_en] = \
                    color if self.get_empty(v_fr, h_fr) == color else self.get_queen(color), self.SPACE, self.SPACE

                self.set_queen(v_to, h_to, color)  # we put a queen if ok

                print(self.print_board())

                if self.find_jump(v_to, h_to, color):

                    a = self.find_jump(v_to, h_to, color)
                    self.input(color, a, 1)
            else:
                print('The cell is not empty or are you trying to eat your pawn')
                self.input(color)

        else:
            print('Pawn is not your color')
            self.input(color)
