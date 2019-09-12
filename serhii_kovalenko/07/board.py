class Board:
    BLACK = 'b'  # black pawn designation
    WHITE = 'w'  # white pawn designation
    B_BLACK = 'B'  # black queen designation
    B_WHITE = 'W'  # white queen designation
    SPACE = '.'  # empty field designation
    SIZE = 8     # board size
    X = {' ': ' ', 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}  # coordinate reference
    Y = {' ': ' ', '1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}  # coordinate reference
    """
    Class describes board
    """
    def __init__(self):
        """
        Init object start board
        """
        self.board = [[' '] * self.SIZE for _ in range(self.SIZE)]
        for i, x in enumerate(self.board):
            for j, y in enumerate(x):
                if (i + j) % 2 != 0 and i < 3:
                    self.board[i][j] = self.BLACK
                elif (i + j) % 2 != 0 and i > 4:
                    self.board[i][j] = self.WHITE
                elif (i + j) % 2 != 0:
                    self.board[i][j] = self.SPACE

    def print_board(self):
        """
        Function to print board
        :return: table with pawn positions
        :rtype: str
        """
        board = ''
        for i, x in enumerate(self.board):

            board += str(self.SIZE - i) + '|'

            for j, y in enumerate(x):

                board += self.board[i][j] + '|'

            board += '\n'

        board += ' '.join(self.X)

        return board

    def position_on_board(self, color='.'):
        """
        Function to coordinates of pawns on the field
        :param color: color pawn
        :type color: str
        :return: table with pawn positions
        :rtype: list
        """
        arm = []
        for x in range(len(self.board)):

            for y in range(len(self.board)):

                if self.board[x][y] == color or self.board[x][y] == self.get_queen(color):
                    arm.append([x, y])

        return arm

    def win(self, bot_color, player_color):
        """
        Function checks for winning by accounting for the number of pawns
        :param bot_color: bot color
        :type bot_color: str
        :param player_color: player color
        :type player_color: str
        :return: bool
        """

        if not self.position_on_board(bot_color):

            print(f'Win mr."{player_color}"')
            return True

        if not self.position_on_board(player_color):

            print(f'Win mr."{bot_color}"')
            return True

        return False
