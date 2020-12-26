def str_board(size, h_grid:list, ley:list) -> str:
    space = ' '
    sign1 = sign2 = sign3 = sign4 = sign5 = sign6 = sign7 = ''
    row1 = row2 = row3 = row4 = row5 = row6 = row7 = row8 = ''
    row1 += space * (size * 2 + 4) + """{}   {}""".format(
            ley[1][0], ley[1][1]) + '\n'
    sign1 += space * (size * 2 + 3) + """/   /""" + '\n'
    row2 += space * ((size - 1) * 2) + """{} - {} - {}""".format(
            ley[0][0], h_grid[0][0], h_grid[0][1])
    if size > 1:
        row2 += space * 3 + """{}""".format(ley[1][2]) + '\n'
        sign2 = space * (size * 2 + 1) + """/ \\ / \\ /""" + '\n'
        row3 += space * ((size - 2) * 2) + """{} - {} - {} - {}""".\
            format(ley[0][1], h_grid[1][0], h_grid[1][1], h_grid[1][2])
    if size > 2:
        row3 += space * 3 + """{}""".format(ley[1][3]) + '\n'
        sign3 = space * ((size - 1) * 2 + 1 ) + """/ \\ / \\ / \\ /""" + '\n'
        row4 += space * ((size - 3) * 2) + """{} - {} - {} - {} - {}""".\
                format(ley[0][2], h_grid[2][0], h_grid[2][1],
                       h_grid[2][2], h_grid[2][3])
    if size > 3:
            row4 += space * 3 + """{}""".format(ley[1][4]) + '\n'
            sign4 = space * ((size - 2) * 2 + 1 )+ """/ \\ / \\ / \\ / \\ /""" + '\n'
            row5 += space * ((size - 4) * 2) + """{} - {} - {} - {} - {} - {}""".\
                format(ley[0][3], h_grid[3][0], h_grid[3][1],
                       h_grid[3][2], h_grid[3][3], h_grid[3][4])
    if size > 4:
        row5 += space * 3 + """{}""".format(ley[1][5]) + '\n'
        sign5 = space * ((size - 3) * 2 + 1 )+ """/ \\ / \\ / \\ / \\ / \\ /""" + '\n'
        row6 += space * ((size - 5) * 2) + """{} - {} - {} - {} - {} - {} - {}""".\
                format(ley[0][4], h_grid[4][0], h_grid[4][1],
                       h_grid[4][2], h_grid[4][3], h_grid[4][4], h_grid[4][5])
    if size == 1:
        sign2 = space * 5 + """\\ / \\""" + '\n'
        row3 += space * 2 + """{} - {}   {}""".\
                format(ley[0][-1], h_grid[-1][0], ley[-1][-1]) + '\n'
        sign3 += space * 7 + """\\""" + '\n'
        row4 += space * 8 + """{}""".format(ley[-1][0]) + '\n'
        result = row1 + sign1 + row2 + '\n' + sign2 + row3 + sign3 + row4
    if size == 2:
        sign3 = space * 5 + """\\ / \\ / \\""" + '\n'
        row4 += space * 2 + """{} - {} - {}   {}""".\
                format(ley[0][-1], h_grid[-1][0], h_grid[-1][1],
                       ley[-1][-1]) + '\n'
        sign4 += space * 7 + """\\   \\""" + '\n'
        row5 += space * 8 + """{}   {}""".format(ley[-1][0], ley[-1][1])
        result = row1 + sign1 + row2 + sign2 + row3 + '\n' + sign3 + row4 +sign4 + row5
    if size == 3:
        sign4 = space * 5 + """\\ / \\ / \\ / \\""" + '\n'
        row5 += space * 2 + """{} - {} - {} - {}   {}""".\
                format(ley[0][-1], h_grid[-1][0], h_grid[-1][1], h_grid[-1][2],
                       ley[-1][-1]) + '\n'
        sign5 += space * 7 + """\\   \\   \\""" + '\n'
        row6 += space * 8 + """{}   {}   {}""".format(ley[-1][0], ley[-1][1], ley[-1][2])
        result = row1 + sign1 + row2 + sign2 + row3 + sign3 + row4 + '\n' + sign4 + row5 + sign5 + row6
    if size == 4:
        sign5 = space * 5 + """\\ / \\ / \\ / \\ / \\""" + '\n'
        row6 += space * 2 + """{} - {} - {} - {} - {}   {}""".\
                format(ley[0][-1], h_grid[-1][0], h_grid[-1][1], h_grid[-1][2],
                       h_grid[-1][3], ley[-1][-1]) + '\n'
        sign6 += space * 7 + """\\   \\   \\   \\""" + '\n'
        row7 += space * 8 + """{}   {}   {}   {}""".format(ley[-1][0], ley[-1][1], ley[-1][2], ley[-1][3])
        result = row1 + sign1 + row2 + sign2 + row3 + sign3 + row4 + sign4 + row5 + '\n' + sign5 + row6 + sign6 + row7
    if size == 5:
        sign6 = space * 5 + """\\ / \\ / \\ / \\ / \\ / \\""" + '\n'
        row7 += space * 2 + """{} - {} - {} - {} - {} - {}   {}""".\
                format(ley[0][-1], h_grid[-1][0], h_grid[-1][1], h_grid[-1][2],
                       h_grid[-1][3], h_grid[-1][4], ley[-1][-1]) + '\n'
        sign7 += space * 7 + """\\   \\   \\   \\   \\""" + '\n'
        row8 += space * 8 + """{}   {}   {}   {}   {}""".format(ley[-1][0], ley[-1][1], ley[-1][2], ley[-1][3], ley[-1][4])
        result = row1 + sign1 + row2 + sign2 + row3 + sign3 + row4 + sign4 + row5 + sign5 + row6 + '\n'+ sign6 + row7 + sign7 + row8
        return result
