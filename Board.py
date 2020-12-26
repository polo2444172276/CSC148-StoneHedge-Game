
class Board:
   def __init__(self, size: int) -> None:

    # Horizontal Grid
        elements_list = [chr(65+x) for x in range((5+size)*size//2)]       #List all the numbers
        item1 = 0
        row_length = 2
        grid = []
        while row_length <= size + 1:
            grid.append([elements_list[item1: item1 + row_length]])
            item1 = item1 + row_length
            row_length += 1
        row_length -= 2
        grid.append([elements_list[item1:item1+row_length]])
    # Left Grid
        left_grid =[]

    if size == 2:
        h_grid = [['A', 'B'],
                  ['C','D','E'],
                  ['F','G']]
    if size == 3:
        h_grid = [['A', 'B'],['C','D','E'],['F','G','H','I'], ['J', 'K', 'L']]
    if size == 4:
        h_grid = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'],
                  ['J', 'K', 'L', 'M', 'N'], ['O', 'P', 'Q', 'R']]
    if size == 5:
        h_grid = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'],
                  ['J', 'K', 'L', 'M', 'N'], ['O', 'P', 'Q', 'R', 'S', 'T']
                  , ['U', 'V','W','X','Y']]
        l_grid = []
        r_grid = []

        if self.size == 1:
            self.h_grid =[['A', 'B'],
                          ['C']]
        if self.size == 2:
            self.h_grid = [['A', 'B'],
                           ['C', 'D', 'E'],
                           ['F', 'G']]
        if self.size == 3:
            self.h_grid = [['A', 'B'],
                           ['C', 'D', 'E'],
                           ['F', 'G', 'H', 'I'],
                           ['J', 'K', 'L']]
        if self.size == 4:
            self.h_grid = [['A', 'B'],
                           ['C', 'D', 'E'],
                           ['F', 'G', 'H', 'I'],
                           ['J', 'K', 'L', 'M', 'N'],
                           ['O', 'P', 'Q', 'R']]

        if self.size == 5:
            self.h_grid = [['A', 'B'],
                           ['C', 'D', 'E'],
                           ['F', 'G', 'H', 'I'],
                           ['J', 'K', 'L', 'M', 'N'],
                           ['O', 'P', 'Q', 'R', 'S', 'T'],
                           ['U', 'V', 'W', 'X', 'Y']]
        # Down and Up Grid
        self.d_grid = [[self.h_grid[i - 1][i + a] for i in range(-a, 0)]
                       + [self.h_grid[-1][a - 1]] for a in
                       range(1, self.size + 1)]
        self.d_grid.append([self.h_grid[i][-1] for i in range(self.size)])
        self.u_grid = [[self.h_grid[i][0] for i in range(self.size)]]
        self.u_grid += [
            [self.h_grid[i + x - 2][x - 1] for i in range(self.size - x + 2)]
            + [self.h_grid[-1][x - 2]] for x in range(2, self.size + 2)]
