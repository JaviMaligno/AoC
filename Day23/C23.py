import numpy as np
from collections import defaultdict
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(23)

def make_grid(text):
    grid = frame(np.where(np.array(list(map(list, text.splitlines()))) == "#", 1, 0))
    elves = list(map(tuple,np.argwhere(grid)))
    return grid, elves

def frame(grid):
    shape = grid.shape
    column = np.zeros(shape[0])
    row = np.zeros(shape[1]+2)
    framed_grid = np.r_[[row],np.c_[column, grid, column],[row]]
    return framed_grid

def round(grid, elves, t):
    proposed_positions = defaultdict(int)
    elves_propose = {}
    move = False
    for elf_index in elves:
        proposed_position = propose_position(elf_index, grid, t)
        elves_propose[elf_index] = proposed_position
        proposed_positions[proposed_position]+=1
    for i,elf_index in enumerate(elves):
        potential_position = elves_propose[elf_index]
        if proposed_positions[potential_position]  < 2:
            # slightly faster if I check if the potential position is different first
            if potential_position != elf_index:
                grid[elf_index] = 0
                grid[potential_position] = 1
                elves[i] = potential_position
                move = True  
    grid, elves = add_frame(grid, elves) 
    return grid, elves, move

def add_frame(grid, elves):
    shape = grid.shape
    first_row = grid[0]
    if np.any(first_row):
        row = np.zeros(shape[1])
        grid = np.r_[[row],grid]
        shape = grid.shape
        elves = list(map(lambda elf: (elf[0]+1, elf[1]), elves))
    last_row = grid[-1]
    if np.any(last_row):
        row = np.zeros(shape[1])
        grid = np.r_[grid,[row]]
        shape = grid.shape
    first_column = grid[:,0]
    if np.any(first_column):
        column = np.zeros(shape[0])
        grid = np.c_[column, grid]
        shape = grid.shape
        elves = list(map(lambda elf: (elf[0], elf[1]+1), elves))
    last_column = grid[:,-1]
    if np.any(last_column):
        column = np.zeros(shape[0])
        grid = np.c_[grid, column]
        shape = grid.shape
    return grid, elves




def sort_list(priorities, t):
    (north_side, north),(south_side,south), (west_side, west), (east_side, east) = priorities
    if t % 4 == 0:
        return (north_side, south_side, west_side, east_side), (north, south, west, east)
    if t % 4 == 1:
        return (south_side, west_side, east_side, north_side), (south, west, east, north)
    if t % 4 == 2:
        return (west_side, east_side, north_side, south_side), (west, east, north, south)
    else:
        return (east_side, north_side, south_side, west_side), (east, north, south, west)

def propose_position(elf_index, grid, t):
    # DEBUG, SOME ELVES ARE APPEARING ON THE FRAME
    north_side, north = grid[elf_index[0]-1, elf_index[1]-1:elf_index[1]+2], (elf_index[0]-1, elf_index[1])
    south_side, south = grid[elf_index[0]+1, elf_index[1]-1:elf_index[1]+2], (elf_index[0]+1, elf_index[1])
    west_side, west = grid[elf_index[0]-1:elf_index[0]+2, elf_index[1]-1], (elf_index[0], elf_index[1]-1)
    east_side , east = grid[elf_index[0]-1:elf_index[0]+2, elf_index[1]+1], (elf_index[0], elf_index[1]+1)
    # I wanted to dynamically put the first element at the end after each round, but for that I would need to define separate methods that compute the sides, and I am too lazy 
    priority, direction = sort_list(((north_side, north),(south_side, south), (west_side, west), (east_side, east)), t)
    if np.any(priority):
        # This could be done with a while loop but it is short enough
        if not np.any(priority[0]):
            proposed_position = direction[0]
        elif not np.any(priority[1]):
            proposed_position = direction[1]
        elif not np.any(priority[2]):
            proposed_position = direction[2]
        elif not np.any(priority[3]):
            proposed_position = direction[3]
        else: 
            proposed_position = elf_index
    else:
        proposed_position = elf_index
    return proposed_position

def progress(text, rounds = None):
    grid, elves = make_grid(text)
    move = True
    if rounds:
        for t in range(rounds):
            grid, elves, move = round(grid, elves, t) 
        rows, columns = grid.shape
        #rectangle = grid[1:rows-2, 1:columns-2]
        #empty = len(np.where( rectangle == 0)[0]) #np where gives the positions as two arrays of coordinates, I just need the amount of coordinates
        empty = (grid.shape[0]-2) * (grid.shape[1]-2) - len(elves)
        return empty,move
    else:
        t = 0
        while move:
            grid, elves, move = round(grid, elves, t)
            t += 1
        return t,grid

print(progress(text)[0])