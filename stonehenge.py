"""
This file contains two subclasses of the game Stonehenge and its
helper functions.
"""
import copy
from game import Game
from game_state import GameState


class Stonehenge(Game):

    """
    This is the subclass of 'Game'.
    This class provides the information about the game
    Stonehenge including:
    1. The instructions of the game
    2. Converts the user input into the valid format
    """

    def __init__(self, p1_starts: bool) -> None:

        """
        Initialize this Game, using p1_starts to find who the first player is
        and initialize the board size
        """

        self.p1_starts = p1_starts
        size = int(input("Choose the board length of the "
                         "game from 1 to 5") + '\n')
        self.current_state = StonehengeState(p1_starts, size)

    def get_instructions(self) -> str:

        """
        Return the instructions for this Game.
        """

        result = """ \n Stonehenge is played on a hexagonal grid formed by \n
                    removing the corners from a triangular grid. Boards \n
                    can have various sizes based on their side-length \n
                    (the number of cells in the grid along the bottom), \n
                    but are always formed in a similar manner: For \n
                    side-length n, the rst row has 2 cells, and each row \n
                    after has 1 additional cell up until there's a row \n 
                    with n + 1 cells, after which the last row has only \n
                    n cells in it. \n
                    Players take turns claiming cells (in the diagram: \n
                    circles labelled with a capital letter). When a player
                    captures at least half of the cells in a ley-line \n
                    (in the diagram: hexagons with a line connecting it \n
                    to cells), then the player captures that ley-line. \n
                    The first player to capture at least half of the \n
                    ley-lines is the winner. A ley-line, once claimed, \n
                    cannot be taken by the other player."""
        return result

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not this game is over at state.
        """

        return state.get_possible_moves() == []

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.
        Precondition: player is 'p1' or 'p2'.
        """
        if self.is_over(self.current_state):
            if self.current_state.get_current_player_name() == player:
                return False
            return True
        return False

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        return string


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.

    WIN - score if player is in a winning position
    LOSE - score if player is in a losing position
    DRAW - score if player is in a tied position
    p1_turn - whether it is p1's turn or not
    """

    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool

    def __init__(self, is_p1_turn: bool, size: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn. Set the board size.
        """
        super().__init__(is_p1_turn)
        self.size = size
        self.h_grid = h_grid(self.size)
        self.d_grid = d_grid(self.h_grid, size)
        self.u_grid = u_grid(self.h_grid, size)
        self.ley = [['@' for i in range(size + 1)],
                    ['@' for i in range(size + 1)],
                    ['@' for i in range(size + 1)]]


    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        >>> print(StonehengeState(True,1))
              @   @
             /   /
        @ - A - B
             \\ / \\
          @ - C   @
               \\
                @"""
        space = ' '
        result = ''
        row1 = row2 = row3 = row4 = row5 = row6 = row7 = row8 = ''
        row1 += space * (self.size * 2 + 4) + """{}   {}""".format(
            self.ley[1][0], self.ley[1][1]) + '\n' + space * \
                (self.size * 2 + 3) + """/   /""" + '\n'
        row2 += space * ((self.size - 1) * 2) + """{} - {} - {}""".format(
            self.ley[0][0], self.h_grid[0][0], self.h_grid[0][1])
        if self.size > 1:
            row2 += space * 3 + """{}""".format(
                self.ley[1][2]) + '\n' + space * (self.size * 2 + 1) \
                    + """/ \\ / \\ /""" + '\n'
            row3 += space * ((self.size - 2) * 2) + """{} - {} - {} - {}""". \
                format(self.ley[0][1], self.h_grid[1][0], self.h_grid[1][1],
                       self.h_grid[1][2])
        if self.size > 2:
            row3 += space * 3 + """{}""".format(self.ley[1][3]) \
                    + '\n' + space * ((self.size - 1) * 2 + 1) \
                    + """/ \\ / \\ / \\ /""" + '\n'
            row4 += space * ((self.size - 3) * 2) \
                    + """{} - {} - {} - {} - {}""".\
                format(self.ley[0][2], self.h_grid[2][0],
                       self.h_grid[2][1],
                       self.h_grid[2][2], self.h_grid[2][3])
        if self.size > 3:
            row4 += space * 3 + """{}""".format(self.ley[1][4]) \
                    + '\n' + space * ((self.size - 2) * 2 + 1) \
                    + """/ \\ / \\ / \\ / \\ /""" + '\n'
            row5 += space * ((self.size - 4) * 2) \
                    + """{} - {} - {} - {} - {} - {}""". \
                        format(self.ley[0][3], self.h_grid[3][0],
                               self.h_grid[3][1],
                               self.h_grid[3][2], self.h_grid[3][3],
                               self.h_grid[3][4])
        if self.size > 4:
            row5 += space * 3 + """{}""".format(
                self.ley[1][5]) + '\n' + space * ((self.size - 3) * 2 + 1) \
                    + """/ \\ / \\ / \\ / \\ / \\ /""" + '\n'
            row6 += space * ((self.size - 5) * 2) \
                    + """{} - {} - {} - {} - {} - {} - {}""". \
                        format(self.ley[0][4], self.h_grid[4][0],
                               self.h_grid[4][1],
                               self.h_grid[4][2], self.h_grid[4][3],
                               self.h_grid[4][4],
                               self.h_grid[4][5])
        if self.size == 1:
            row2 += '\n' + space * 5 + """\\ / \\""" + '\n'
            row3 += space * 2 + """{} - {}   {}""". \
                format(self.ley[0][-1], self.h_grid[-1][0],
                       self.ley[-1][-1]) + '\n' + space * 7 + """\\""" + '\n'
            row4 += space * 8 + """{}""".format(self.ley[-1][0])
            result = row1 + row2 + row3 + row4
        if self.size == 2:
            row3 += '\n' + space * 5 + """\\ / \\ / \\""" + '\n'
            row4 += space * 2 + """{} - {} - {}   {}""". \
                format(self.ley[0][-1], self.h_grid[-1][0], self.h_grid[-1][1],
                       self.ley[-1][-1]) + '\n' + space * 7 \
                    + """\\   \\""" + '\n'
            row5 += space * 8 + """{}   {}""".format(self.ley[-1][0],
                                                     self.ley[-1][1])
            result = row1 + row2 + row3 + row4 + row5
        if self.size == 3:
            row4 += '\n' + space * 5 + """\\ / \\ / \\ / \\""" + '\n'
            row5 += space * 2 + """{} - {} - {} - {}   {}""". \
                format(self.ley[0][-1], self.h_grid[-1][0], self.h_grid[-1][1],
                       self.h_grid[-1][2],
                       self.ley[-1][-1]) + '\n' + space * 7 \
                    + """\\   \\   \\""" + '\n'
            row6 += space * 8 + """{}   {}   {}""".format(self.ley[-1][0],
                                                          self.ley[-1][1],
                                                          self.ley[-1][2])
            result = row1 + row2 + row3 + row4 + row5 + row6
        if self.size == 4:
            row5 += '\n' + space * 5 + """\\ / \\ / \\ / \\ / \\""" + '\n'
            row6 += space * 2 + """{} - {} - {} - {} - {}   {}""". \
                format(self.ley[0][-1], self.h_grid[-1][0], self.h_grid[-1][1],
                       self.h_grid[-1][2],
                       self.h_grid[-1][3], self.ley[-1][-1]) + '\n' + \
                    space * 7 + """\\   \\   \\   \\""" + '\n'
            row7 += space * 8 + """{}   {}   {}   {}""".format(self.ley[-1][0],
                                                               self.ley[-1][1],
                                                               self.ley[-1][2],
                                                               self.ley[-1][3])
            result = row1 + row2 + row3 + row4 + row5 + row6 + row7
        if self.size == 5:
            row6 += '\n' + space * 5 + """\\ / \\ / \\ / \\ / \\ / \\""" + '\n'
            row7 += space * 2 + """{} - {} - {} - {} - {} - {}   {}""". \
                format(self.ley[0][-1], self.h_grid[-1][0], self.h_grid[-1][1],
                       self.h_grid[-1][2],
                       self.h_grid[-1][3], self.h_grid[-1][4],
                       self.ley[-1][-1]) + '\n' + space * 7 \
                    + """\\   \\   \\   \\   \\""" + '\n'
            row8 += space * 8 + """{}   {}   {}   {}   {}""".format(
                self.ley[-1][0],
                self.ley[-1][1],
                self.ley[-1][2],
                self.ley[-1][3],
                self.ley[-1][4])
            result = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8
        return result



    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        >>> state = StonehengeState(True, 2)
        >>> print(state.make_move("A").get_possible_moves())
        ['B', 'C', 'D', 'E', 'F', 'G']
        >>> state = StonehengeState(True, 1)
        >>> print(state.make_move("A").get_possible_moves())
        []
        """
        possible_moves = []

        for letter in sum(self.h_grid, []):
            if letter != 1 and letter != 2:
                possible_moves.append(letter)

        # Check conditions for game over
        sum_ley = sum(self.ley, [])
        player1 = [i for i in sum_ley if i == 1]
        player2 = [x for x in sum_ley if x == 2]
        if len(player1) >= len(sum_ley)/2 or len(player2) >= len(sum_ley)/2:
            possible_moves = []
        return possible_moves


    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        >>> print(StonehengeState(True,1).get_current_player_name == 'p1')
        False
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: str) -> 'GameState':
        """
        Return the GameState that results from applying move to this GameState.
        >>> state = StonehengeState(True, 1)
        >>> print(state.make_move("A"))
              1   @
             /   /
        1 - 1 - B
             \\ / \\
          @ - C   @
               \\
                1"""

        new_state = copy.deepcopy(self)

        # Change and mark the cell
        new_state.h_grid = change_grid(self.h_grid, move, new_state.p1_turn)

        # Update Down and Up Grid
        new_state.u_grid = u_grid(new_state.h_grid, new_state.size)
        new_state.d_grid = d_grid(new_state.h_grid, new_state.size)

        # Leyline Checker
        new_state.ley[0] = ley_checker(new_state.h_grid, new_state.ley[0])
        new_state.ley[1] = ley_checker(new_state.u_grid, new_state.ley[1])
        new_state.ley[-1] = ley_checker(new_state.d_grid, new_state.ley[-1])

        # Switch Turn
        new_state.p1_turn = not new_state.p1_turn
        return new_state

    def is_valid_move(self, move: str) -> bool:
        """
        Return whether move is a valid move for StonehengeState.
        >>> state = StonehengeState(True, 1)
        >>> print('D' in state.get_possible_moves())
        False
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        >>> state = StonehengeState(True, 1)
        >>> state.__repr__()
        "P1's Turn: True - Board Size: 1 - Total Leylines: 6 -
        Total Leylines Claimed by P1 - 0 - Total Leylines
        Claimed by P2 - 0 - Available Moves ['A', 'B', 'C']"
        """

        return "P1's Turn: {} - Board Size: {} - Total " \
               "Leylines: {} - Total Leylines Claimed by P1 " \
               "- {} - Total Leylines Claimed by P2 - {} " \
               "- Available Moves {}".\
            format(self.p1_turn, self.size, (self.size + 1)*3,
                   sum(self.ley, []).count(1), sum(self.ley, []).count(2),
                   self.get_possible_moves())

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        >>> state = StonehengeState(True, 2)
        >>> state = state.make_move("A")
        >>> state.rough_outcome()
        0
        """
        temp = copy.deepcopy(self)
        temp1 = [temp.make_move(move) for move in temp.get_possible_moves()]
        if player_win(self):
            return self.WIN
        elif all([player_win(temp2) for temp2 in temp1]):
            return self.LOSE
        return self.DRAW


#helper functions
def player_win(state: 'StonehengeState') -> bool:
    """
    >>> new_state = StonehengeState(True, 1)
    >>> new_state = new_state.make_move("A")
    >>> player_win(new_state)
    False
    """
    temp = copy.deepcopy(state)

    temp1 = [temp.make_move(move) for move in temp.get_possible_moves()]

    if any([temp2.get_possible_moves() == [] for temp2 in temp1]):
        return True
    return False


def h_grid(size: int) -> list:
    """
    Return a nested list that represents the horizontal grid of the board
    depending on the size.
    >>> state = StonehengeState(True, 1)
    >>> print(state.h_grid)
    [['A', 'B'], ['C']]
    """

    letter_list = [chr(65 + x) for x in range((5 + size) * size // 2)]
    first = 0
    new_grid = []
    for num in range(2, size + 2):
        new_grid += [letter_list[first: first + num]]
        first += num
    new_grid += [letter_list[first:]]
    return new_grid


def d_grid(grid: list, size: int) -> list:
    """
    Return a nested list that represents the down grid of the board
    depending on the size and the horizontal grid
    >>> state = StonehengeState(True, 1)
    >>> print(state.d_grid)
    [['A', 'C'], ['B']]
    """
    temp = copy.deepcopy(grid)
    new_grid = [[temp[i - 1][i + a] for i in range(0 - a, 0)]
                + [temp[-1][a - 1]] for a in range(1, size + 1)]
    new_grid.append([temp[i][-1] for i in range(size)])
    return new_grid


def u_grid(grid: list, size: int) -> list:
    """
    Return a nested list that represents the down grid of the board
    depending on the size and the horizontal grid
    >>> state = StonehengeState(True, 1)
    >>> print(state.u_grid)
    [['A'], ['B', 'C']]
    """
    temp = copy.deepcopy(grid)
    new_grid = [[temp[i][0] for i in range(size)]]
    new_grid += [[temp[i + x - 2][x - 1] for i in range(size - x + 2)]
                 + [temp[-1][x - 2]] for x in range(2, size + 2)]
    return new_grid

def change_grid(grid: list, move: str, is_p1_turn: bool) -> list:
    """
    Modify the horizontal grid during the GameState if player makes a move
    >>> state = StonehengeState(True, 1)
    >>> change_grid(state.h_grid, 'A', True)
    [[1, 'B'], ['C']]
    """
    new_grid = copy.deepcopy(grid)
    for sublist in new_grid:
        for letter in sublist:
            if letter == move:
                new_grid[new_grid.index(sublist)][sublist.index(move)] = 1 \
                    if is_p1_turn else 2
    return new_grid

def ley_checker(grid: list, leyline: list) -> list:
    """
    Checks and Modifies the leyliness during the GameState if player's move
    leads to a change in leyline
    >>> state = StonehengeState(True, 1)
    >>> new_state = state.make_move('A')
    >>> print(new_state.ley)
    [[1, '@'], [1, '@'], [1, '@']]
    """
    new_ley = copy.deepcopy(leyline)
    for row in grid:
        if new_ley[grid.index(row)] == '@':
            integer = [i for i in row if type(i) == int]
            if integer.count(1) >= len(row)/2:
                new_ley[grid.index(row)] = 1
            if integer.count(2) >= len(row)/2:
                new_ley[grid.index(row)] = 2
    return new_ley


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
