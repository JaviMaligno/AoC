import numpy as np
from collections import defaultdict
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(23)

def make_grid(text):
    grid = frame(np.where(np.array(list(map(list, text.splitlines()))) == "#", 1, 0))
    elves = np.argwhere(grid)
    return grid, elves

def frame(grid):
    shape = grid.shape
    column = np.zeros(shape[0])
    row = np.zeros(shape[1]+2)
    framed_grid = np.r_[[row],np.c_[column, grid, column],[row]]
    return framed_grid

def round(grid, elves):
    proposed_positions = defaultdict(int)
    elves_propose = {}
    for elve_index in elves:
        proposed_position = propose_position(elve_index, grid)
        elves_propose[elve_index] = proposed_position
        proposed_positions[proposed_position]+=1
    for i,elve_index in enumerate(elves):
        potential_position = elves_propose[elve_index]
        if proposed_positions[potential_position]  < 2:
            grid[elve_index[0], elve_index[1]] = 0
            grid[proposed_position] = 1
            elves[i] = potential_position
    add_frame(grid)
    return grid, elves

        
def add_frame(grid):
    pass
def propose_position(elve_index, grid):
    pass

def progress(text, rounds = 10):
    grid, elves = make_grid(text)
    for t in range(10):
        grid, elves = round(grid, elves) 
    rows, columns = grid.shape
    empty = np.sum(np.where(grid[1:rows-2, 1:columns-2] == 0))
    return empty