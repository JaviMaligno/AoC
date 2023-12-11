import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(10)


from math import ceil

def find_cycle_length(grid):
    # Find the starting position 'S'
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)

    # Define the directions for each type of pipe
    directions = {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, 1), (0, -1)],
        'L': [(0, 1), (-1, 0)],
        'J': [(0, -1), (-1, 0)],
        '7': [(0, -1), (1, 0)],
        'F': [(0, 1), (1, 0)]
    }

    # Define the pipes that can connect to each direction
    connectable_pipes = {
        (1, 0): ['|', '7', 'F'],  # South
        (-1, 0): ['|', 'L', 'J'],  # North
        (0, 1): ['-', 'L', 'F'],  # East
        (0, -1): ['-', '7', 'J']  # West
    }

    # Determine the connections of 'S' dynamically
    s_directions = []
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_position = (start[0] + direction[0], start[1] + direction[1])
        next_pipe = grid[next_position[0]][next_position[1]]
        if next_pipe in connectable_pipes[(-direction[0], -direction[1])]:  # Check the opposite direction
            s_directions.append(direction)
    directions['S'] = s_directions

    # Start the cycle from one neighbor of 'S'
    cycle_length = 1  # Count the 'S' tile
    current_position = (start[0] + s_directions[0][0], start[1] + s_directions[0][1])
    previous_position = start

    while True:
        cycle_length += 1
        pipe = grid[current_position[0]][current_position[1]]
        for direction in directions[pipe]:
            next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            next_pipe = grid[next_position[0]][next_position[1]]
            # Check if the next position is the start before checking if the next pipe is connectable
            if next_position == start:
                return ceil(cycle_length/2)   # Return the cycle length if the next position is the start
            elif next_position != previous_position and next_pipe in connectable_pipes[(-direction[0], -direction[1])]:
                previous_position = current_position
                current_position = next_position
                break






grid = [
    "-L|F7",
    "7S-7|",
    "L|7||",
    "-L-J|",
    "L|-J"
]
distance = find_cycle_length(grid)
#print(distance)

# Define the grid
grid = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ..."
]

# Call the function
#distance = find_cycle_length(grid)

# Print the result
#print(distance)


grid = text.splitlines()

#distance = find_cycle_length(grid)

#print(distance)

def find_enclosed_tiles(grid):
    # Find the starting position 'S'
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)

    # Define the directions for each type of pipe
    directions = {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, 1), (0, -1)],
        'L': [(0, 1), (-1, 0)],
        'J': [(0, -1), (-1, 0)],
        '7': [(0, -1), (1, 0)],
        'F': [(0, 1), (1, 0)]
    }

    # Define the pipes that can connect to each direction
    connectable_pipes = {
        (1, 0): ['|', '7', 'F'],  # South
        (-1, 0): ['|', 'L', 'J'],  # North
        (0, 1): ['-', 'L', 'F'],  # East
        (0, -1): ['-', '7', 'J']  # West
    }

    # Determine the connections of 'S' dynamically
    s_directions = []
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_position = (start[0] + direction[0], start[1] + direction[1])
        next_pipe = grid[next_position[0]][next_position[1]]
        if next_pipe in connectable_pipes[(-direction[0], -direction[1])]:  # Check the opposite direction
            s_directions.append(direction)
    directions['S'] = s_directions

    # Start the cycle from one neighbor of 'S'
    loop_positions = [start]
    current_position = (start[0] + s_directions[0][0], start[1] + s_directions[0][1])
    previous_position = start

    while True:
        loop_positions.append(current_position)
        pipe = grid[current_position[0]][current_position[1]]
        for direction in directions[pipe]:
            next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            next_pipe = grid[next_position[0]][next_position[1]]
            if next_position == start:
                return find_enclosed_tiles_by_loop(grid, loop_positions)  # Return the number of enclosed tiles
            elif next_position != previous_position and next_pipe in connectable_pipes[(-direction[0], -direction[1])]:
                previous_position = current_position
                current_position = next_position
                break


def find_enclosed_tiles_by_loop(grid, loop_positions):
    enclosed_tiles = 0
    for i in range(len(grid)):
        loop_positions_in_row = [pos for pos in loop_positions if pos[0] == i and grid[pos[0]][pos[1]] != '-']
        loop_positions_in_row.sort(key=lambda pos: pos[1])
        for j in range(0, len(loop_positions_in_row) - 1, 2):  # Skip every other loop pipe
            if loop_positions_in_row[j][1] + 1 < loop_positions_in_row[j + 1][1]:
                enclosed_tiles += len([k for k in range(loop_positions_in_row[j][1] + 1, loop_positions_in_row[j + 1][1]) if (i, k) not in loop_positions])
    return enclosed_tiles


def find_loop_positions(grid):
    # Find the starting position 'S'
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)

    # Define the directions for each type of pipe
    directions = {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, 1), (0, -1)],
        'L': [(0, 1), (-1, 0)],
        'J': [(0, -1), (-1, 0)],
        '7': [(0, -1), (1, 0)],
        'F': [(0, 1), (1, 0)]
    }

    # Define the pipes that can connect to each direction
    connectable_pipes = {
        (1, 0): ['|', '7', 'F'],  # South
        (-1, 0): ['|', 'L', 'J'],  # North
        (0, 1): ['-', 'L', 'F'],  # East
        (0, -1): ['-', '7', 'J']  # West
    }

    # Determine the connections of 'S' dynamically
    s_directions = []
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_position = (start[0] + direction[0], start[1] + direction[1])
        next_pipe = grid[next_position[0]][next_position[1]]
        if next_pipe in connectable_pipes[(-direction[0], -direction[1])]:  # Check the opposite direction
            s_directions.append(direction)
    directions['S'] = s_directions

    # Start the cycle from one neighbor of 'S'
    loop_positions = [start]
    current_position = (start[0] + s_directions[0][0], start[1] + s_directions[0][1])
    previous_position = start

    while True:
        loop_positions.append(current_position)
        pipe = grid[current_position[0]][current_position[1]]
        for direction in directions[pipe]:
            next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            next_pipe = grid[next_position[0]][next_position[1]]
            if next_position == start:
                return loop_positions  # Return the positions of the loop pipes
            elif next_position != previous_position and next_pipe in connectable_pipes[(-direction[0], -direction[1])]:
                previous_position = current_position
                current_position = next_position
                break



input_text = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

input_text_2 = """
..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
"""

input_text_3 = """
OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
"""

def highlight_loop(input_text, loop_positions):
    # Convert the input text to a list of lists
    grid = [list(row) for row in input_text.splitlines()]

    # Highlight the loop pipes
    for pos in loop_positions:
        i, j = pos
        grid[i][j] = '#'  # Use '#' to highlight the loop pipe

    # Convert the grid back to a string
    output_text = '\n'.join(''.join(row) for row in grid)

    return output_text


grid = input_text_3.splitlines()
grid_list = list(map(lambda x: x.split(), grid))
#grid = text.splitlines()
loop_positions = find_loop_positions(grid)
print(loop_positions)
print(highlight_loop(input_text_3, loop_positions))


print(grid[1:])


def count_tiles(grid, loop):
    # Convert loop to a set for O(1) lookups
    loop_set = set(loop)

    # Sort the loop points by their x-coordinate (row index) and then by their y-coordinate (column index)
    sorted_loop = sorted(loop, key=lambda point: (point[0], point[1]))

    # Initialize count of tiles inside the loop
    count = 0

    # Create an alternative boundary list without horizontal lines
    alt_loop = [point for point in sorted_loop if grid[point[0]][point[1]] != "-"]

    # Sort the alternative list by their x-coordinate (row index) and then by their y-coordinate (column index)
    alt_loop = sorted(alt_loop, key=lambda point: (point[0], point[1]))

    # Go through each row in the grid
    for x, row in enumerate(grid):
        # Get the loop points on this row from the alternative list
        row_points = [point for point in alt_loop if point[0] == x]

        # If there are no loop points on this row, continue to the next row
        if not row_points:
            continue

        # Go through the row points in pairs
        for i in range(0, len(row_points), 2):
            # If there is no next point, break the loop
            if i+1 >= len(row_points):
                break

            # Get the start and end points of the current pair
            start, end = row_points[i][1], row_points[i+1][1]

            # Count the tiles between the start and end points
            for y in range(start+1, end):
                if (x, y) not in loop_set:
                    count += 1

    return count





print(count_tiles(grid, loop_positions))


