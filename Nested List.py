y = [['A', 'B'],
     ['C', 'D', 'E'],
     [1, 1, 1, 1],
     [2, 2, 1, 1, 'N'],
     [1, 1, 1, 2, 2, 2],
     ['U', 5, 6, 'X', 'Y']]
leyline = [['@' for i in range(6)]] * 3  # h, u, d
def change_grid(grid: list, move: str, is_p1_turn: bool) -> None:

    for sublist in grid:
        for letter in sublist:
            if letter == move:
                if is_p1_turn:
                    grid[grid.index(sublist)][sublist.index(move)] = 1
                else:
                    grid[grid.index(sublist)][sublist.index(move)] = 2

def leyline_checker(grid:list, leyline: list, is_p1_turn:bool) -> None:
    for sublist in grid:
        acc = 0
        for item in sublist:
            if is_p1_turn:
                if item == 1:
                    acc += 1
                else:
                    acc += 0
                if acc >= len(sublist)//2:
                    leyline[0][grid.index(sublist)] = 1
            else:
                if item == 2:
                    acc += 1
                else:
                    acc += 0
                if acc >= len(sublist)//2:
                    leyline[0][grid.index(sublist)] = 1


   # if letter == move:
    #    if is_p1_turn:
     #       grid[grid.index(sublist)][sublist.index(move)] = 1
     #   else:
      #      grid[grid.index(sublist)][sublist.index(move)] = 2
      #  return grid
    # else:
      #  return [[change_grid(letter, move, is_p1_turn) for letter in sublist] for sublist in grid]]



def ley_checker(grid:list, leyline:list) -> list:
    for row in grid:
        integer = [i for i in row if type(i) == int]
        if integer.count(1) >= len(row)/2 and leyline[grid.index(row)].\
                isdigit() is False:
            leyline[grid.index(row)] = 1
        elif integer.count(2) >= len(row)/2 and leyline[grid.index(row)].\
                isdigit() is False:
            leyline[grid.index(row)] = 2
    return leyline
def h_grid(size: int) -> list:
    letter_list = [chr(65 + x) for x in
               range((5 + size) * size // 2)]
    row_s, row_e = 0, 2
    new_grid = []
    while row_e <= size + 1:
        new_grid.append(letter_list[row_s: row_s + row_e])
        row_s += row_e
        row_e += 1
    row_e -= 2
    new_grid.append(letter_list[row_s:row_s + row_e])
    return new_grid
print(ley_checker(y, leyline[0]))


def ley3_checker(grid: list, leyline:list) -> list:
    new_ley = leyline
    for ley in new_ley:
        if not isinstance(ley, int):
            integer = [i for i in grid[ley] if type(i) == int]
            if integer.count(1) >= len(grid[ley]) / 2:
                new_ley[index(ley)] = 1
            elif integer.count(2) >= len(grid[ley])/ 2:
                new_ley[index(ley)] = 2
        return new_ley

def ley1_checker(grid: list, leyline: list) -> None:
    for row in grid:
        acc1 = 0
        acc2 = 0
        for element in row:
            if element == 1:
                acc1 += 1
            if element == 2:
                acc2 += 1
            if leyline[grid.index(row)] == '@':
                if acc1 >= len(row)/2 and acc2 < len(row)/2:
                    leyline[grid.index(row)] = 1
                if acc2 >= len(row)/2 and acc1 < len(row)/1:
                    leyline[grid.index(row)] = 2
