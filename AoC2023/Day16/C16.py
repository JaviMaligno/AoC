import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(16)

def trace_beam(grid, start_beam):
    directions = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0)}
    mirror_reflections = {'/': {'up': 'right', 'right': 'up', 'down': 'left', 'left': 'down'},
                          '\\': {'up': 'left', 'left': 'up', 'down': 'right', 'right': 'down'}}
    splitter_reflections = {'|': {'right': ['up', 'down'], 'left': ['up', 'down']},
                            '-': {'up': ['right', 'left'], 'down': ['right', 'left']}}
    visited = set()
    beams = [start_beam]
    used_beams = set()

    while beams:
        new_beams = []
        for x, y, direction in beams:
            while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] in '/\\':
                    direction = mirror_reflections[grid[x][y]][direction]
                elif grid[x][y] in '|-':
                    if direction in splitter_reflections[grid[x][y]]:
                        for new_direction in splitter_reflections[grid[x][y]][direction]:
                            if (x, y, new_direction) not in used_beams:
                                new_beams.append((x, y, new_direction))
                                used_beams.add((x, y, new_direction))
                        break
                if (x, y) not in visited:
                    visited.add((x, y))
                dx, dy = directions[direction]
                x += dx
                y += dy
        beams = new_beams
    return len(visited)

grid = [
    '.|...\\....',
    '|.-.\\.....',
    '.....|-...',
    '........|.',
    '..........',
    '.........\\',
    '..../.\\\\..',
    '.-.-/..|..',
    '.|....-|.\\',
    '..//.|....'
]




grid = text.splitlines()
#visited_count, grid_copy = trace_beam(grid)
#visited_count = trace_beam(grid, (0,0,"right"))
#print('Visited count:', visited_count)
#print('Grid:')
#for row in grid_copy:
#    print(''.join(row))

def max_trace_beam(grid):
    max_visited = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0:
                start_directions = ['down']
            elif i == len(grid) - 1:
                start_directions = ['up']
            elif j == 0:
                start_directions = ['right']
            elif j == len(grid[0]) - 1:
                start_directions = ['left']
            else:
                continue

            for start_direction in start_directions:
                start_beam = (i, j, start_direction)
                visited = trace_beam(grid, start_beam)
                max_visited = max(max_visited, visited)
    return max_visited



print(max_trace_beam(grid))