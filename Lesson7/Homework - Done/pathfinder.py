Map = [
   # 0 1 2 3 4 5 6 7 8 9
    [1,0,1,1,1,1,1,1,1,1], # 0
    [1,0,0,0,1,0,0,0,0,1], # 1
    [1,1,1,0,1,1,1,0,1,1], # 2
    [1,0,0,0,1,0,0,0,0,1], # 3
    [1,0,1,1,1,0,1,0,1,1], # 4
    [1,0,0,0,0,0,1,0,0,1], # 5
    [1,0,1,1,1,1,1,1,0,1], # 6
    [1,0,1,0,1,0,0,0,0,1], # 7
    [1,0,0,0,1,0,1,0,0,1], # 8
    [1,1,1,1,1,0,1,1,1,1]  # 9
]

def valid_neighbours(map, row, col):
    possible = list((row+i, col+j) \
        for i, j in [(-1,0),(0,-1),(1,0),(0,1)])
    inside_map = list(pos for pos in possible \
        if pos[0] >= 0 and pos[1] >= 0 and \
        pos[0] < len(map) and pos[1] < len(map[0]))
    valid = list(pos for pos in inside_map \
        if map[pos[0]][pos[1]] == 0)
    return valid

def find_path(map, row_from, col_from, row_to, col_to):
    map[row_from][col_from] = 2
    if (row_from, col_from) == (row_to, col_to): # row_from == row_to and col_from == col_to
        print(row_from, col_from)
        return True
    
    valid = valid_neighbours(map, row_from, col_from)
    for pos in valid:
        row, col = pos
        found = find_path(map, row, col, row_to, col_to)
        if found is True:
            print(row_from, col_from)
            return True
    
    return False

find_path(Map, 0, 1, 9, 5)
