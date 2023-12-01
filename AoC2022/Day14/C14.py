import numpy as np
from collections import defaultdict
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(14)
# I will just store rock positions, iif it is very slow I will compute max and min width (I believe 490 is the min) and the feed it into a numpy array
def lines(text):
    return list(map(lambda line: list(map(lambda x: tuple(map(int,x.split(','))),line.split(' -> '))),text.splitlines()))

def default_value():
    return defaultdict(bool)

def generate_rocks(init, end, dictionary):
    init_column = init[0]
    init_row = init[1]
    end_column = end[0]
    end_row = end[1]

    if init_column == end_column:
        for j in range(min(init_row, end_row ), max(init_row, end_row )+1):
            dictionary[init_column][j] = 'R'
    elif init_row == end_row :
        for i in range(min(init_column, end_column), max(init_column,end_column)+1):
            dictionary[i][init_row] = 'R'
    

def set_rocks(lines):
    rocks = defaultdict(default_value)
    for line in lines:
        for init, end in zip(line[:-1], line[1:]):
            generate_rocks(init,end,rocks)
    return rocks

def floor(rocks):
    maxs = defaultdict(int)
    for k,v in rocks.items():
        maxs[k] = max(v.keys())
    max_height = max(h for (c,h) in maxs.items())
    return max_height+2



def no_block(current_col, rocks):
    column = rocks[current_col]
    blocks = any(column[i] for i in column.keys())
    return not blocks

def sand_one_move(current_position, rocks, max_depth=np.inf):
    REST = False
    current_col = current_position[0]
    current_row = current_position[1]
    #I can skip thee first one
    #if not rocks[current_col][current_row+1]:
        #vertical = np.array([0,-1])
        #current_position += vertical

    if current_row +1 < max_depth:
        if not rocks[current_col-1][current_row+1]:
            left_diag = np.array([-1,1])
            current_position += left_diag
        elif not rocks[current_col+1][current_row+1]:
            right_diag = np.array([1,1])
            current_position += right_diag
        else:
            REST = True
    else:
        REST = True
    return current_position, REST

def sand_move(rocks, max_depth = np.inf):
    START = np.array([500,0])
    current_position = START.copy()
    
    REST = False
    while not REST:
        #if no_block(current_position[0],rocks):
        current_col = current_position[0]
        current_row = current_position[1]
        column = rocks[current_col]
        max_row = min([max_depth]+[i for i in column.keys() if column[i] and i >= current_row])
         #presort this so that I just havve to check the first
                          # I can also presave  the mins and then update them at rest
        if max_row <= 0:
            break
        else: 
            current_position[1] = max_row-1 
        
            current_position, REST = sand_one_move(current_position, rocks, max_depth = max_depth)

    if REST:
        rocks[current_position[0]][current_position[1]] = 'S'
    return REST # I can add booleans into integers later

def count_rest(rocks, limit_depth=True):
    REST = True
    max_depth = floor(rocks) if limit_depth else np.inf
    grains = 0
    while REST:
        REST = sand_move(rocks, max_depth = max_depth)
        grains += REST
        print(grains)
    return  grains
        

instructions = lines(text)
rocks = set_rocks(instructions)
#print(rocks[189].keys())
print(count_rest(rocks))
#print(no_block(189,rocks))
#print(floor(rocks))