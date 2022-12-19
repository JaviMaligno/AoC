import numpy as np
#from itertools import tee
from math import lcm
from rocks import BOARD, ROCKS
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(17)

def tetris(text, board, rocks, n_rocks):
    max_height = 0
    i = 0
    states = []
    # jets, current_jets = iter(text) #aparently it is slow to make copies of generators
    jets = text.replace("\n", "")
    jet_index = 0
    while i < n_rocks:
        rock = rocks[i % 5]()
        #jets = drop_rock(rock, board, current_jets, initial_jet = jets)
        max_height, jet_index, states = drop_rock(rock, board, jets, jet_index, max_height, i, states)
        i += 1
        #board = np.concatenate((np.zeros(4,7),board))
        board = stack_board(board, max_height)
    return max_height, board, states

def stack_board(board, max_height):
    depth = board.shape[0] #may compute it before since I use it in two functions
    diff = depth - max_height
    rows = 4 - diff
    board = np.concatenate((np.zeros((rows, 7)), board)) if rows else board
    return board
    
def move_rock(rock, jet, row, board):
    if jet == '<':
        rock.left(row, board)
    elif jet == '>':
        rock.right(row, board)
    else:
        raise ValueError('Jet not implemented')

def drop_rock(rock, board, jets, jet_index, max_height, i, states, initial_jet  = None):
    rested = rock.rested
    row = 0
    pattern_size = len(jets)
    
    while not rested:
        jet = jets[jet_index % pattern_size]
        move_rock(rock,jet, row, board)
        row = rock.down(row, board)
        rested = rock.rested
        jet_index += 1
    if all(board[row]):
        number = i+1
        type = rock.name
        states.append([number, type])
    

    depth = board.shape[0]
    curent_height = (depth - row) + rock.height - 1
    max_height = max(curent_height, max_height)
    return max_height, jet_index, states
        # using generators, which happenss to be slower  and more memory consuming if we consume a generator before using the copy
""" try:
            jet = next(current_jets)
            move_rock(rock,jet)
            row = rock.down(row, board)
            rested = rock.rested
        except StopIteration:
            initial_jets, current_jets = tee(initial_jet)
            jet = next(current_jets)
            row = rock.down(row, board)
            rested = rock.rested """
    

pattern = tetris(text, BOARD, ROCKS, 521)[0] #521 rocks: height = 830; 2271 rocks: height=3626  -> every 1750 rocks heights increases by 2796
# 1000000000000 rocks. First 521 to start the pattern -> height 830, rocks left: 999999999479 -> divide by 1750 -> 571428571 times plus 229 rockss remaining (they add)
# 521+229 rocks : height 1182, the additional height is 1182-830=352
print(pattern)
"""
for i in range(board.shape[0]):
    if all(board[i]):
        print(i) """
#print(lcm(len(text),5))
#521+(2271-521)
