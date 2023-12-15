import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(14)


def move_Os_up(grid):
    # Convert the grid to a list of lists for easier manipulation
    grid = [list(row) for row in grid]

    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Iterate over each column
    for j in range(cols):
        # Find all the 'O's, '.'s and '#'s in the column
        column = [grid[i][j] for i in range(rows)]
        Os = [i for i, x in enumerate(column) if x == 'O']
        dots = [i for i, x in enumerate(column) if x == '.']
        hashes = [i for i, x in enumerate(column) if x == '#']

        # If there are no 'O's or no '.'s, move on to the next column
        if not Os or not dots:
            continue

        # Move each 'O' up as far as possible
        for i in range(len(Os)-1, -1, -1):
            # Find the highest '.' above the current 'O' and below any '#'
            available_dots = [d for d in dots if d < Os[i] and (not [h for h in hashes if h < Os[i]] or d > max(h for h in hashes if h < Os[i]))]
            while available_dots:
                highest_dot = max(available_dots)

                # Swap the 'O' and the highest '.'
                grid[highest_dot][j], grid[Os[i]][j] = grid[Os[i]][j], grid[highest_dot][j]

                # Update the positions of the 'O's and '.'s
                Os[i] = highest_dot
                dots.remove(highest_dot)
                dots.append(Os[i])

                # Check if there are more '.'s above the current 'O' and below any '#'
                available_dots = [d for d in dots if d < Os[i] and (not [h for h in hashes if h < Os[i]] or d > max(h for h in hashes if h < Os[i]))]

    # Convert the grid back to the original format
    return [''.join(row) for row in grid]


def calculate_score(grid):
    # Convert the grid to a list of lists for easier manipulation
    grid = [list(row) for row in grid]

    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize the score
    score = 0

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell contains an 'O', add its score to the total score
            if grid[i][j] == 'O':
                score += rows - i

    return score
""" def rotate_grid(grid, angle):
    if angle not in [90, 180, 270]:
        return "Invalid angle. Angle must be 90, 180, or 270."
    
    rotated_grid = grid
    for _ in range(angle // 90):
        rotated_grid = [''.join(x[::-1]) for x in zip(*rotated_grid)]
    
    return rotated_grid """

def rotate_grid(grid, angle):
    if angle not in [90, 180, 270]:
        return "Invalid angle. Angle must be 90, 180, or 270."
    
    if angle == 90:
        # 90 degree rotation is equivalent to reversing the rows and then transposing the grid
        rotated_grid = [''.join(x[::-1]) for x in zip(*grid)]
    elif angle == 180:
        # 180 degree rotation is equivalent to reversing both the rows and the columns
        rotated_grid = [row[::-1] for row in grid[::-1]]
    elif angle == 270:
        # 270 degree rotation is equivalent to transposing the grid and then reversing the rows
        rotated_grid = [''.join(x) for x in zip(*grid)][::-1]
    
    return rotated_grid







def move_Os(grid, direction):
    if direction == 'up':
        return move_Os_up(grid)
    elif direction == 'right':
        return rotate_grid(move_Os_up(rotate_grid(grid, 270)), 90)
    elif direction == 'down':
        return rotate_grid(move_Os_up(rotate_grid(grid, 180)), 180)
    elif direction == 'left':
        return rotate_grid(move_Os_up(rotate_grid(grid, 90)), 270)


grid = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#...."
]

""" print("Original grid:")
for row in grid:
    print(row)
print()

directions = ["up", "left", "down", "right"]
directions = [90, 180, 270]
for direction in directions:
    new_grid = rotate_grid(grid, direction)
    print(f"After moving Os {direction}:")
    for row in new_grid:
        print(row)
    print() """

#score = calculate_score(new_grid)
#print(f"The total score is {score}")


#grid = text.splitlines()
#new_grid = move_Os_up(grid)
#score = calculate_score(new_grid)
#print(score)



""" left_rotated_grid = rotate_grid(grid, 90)
print("Grid rotated 90 degrees clockwise (equivalent to a left move):")
for row in left_rotated_grid:
    print(row)
print()
 """
def count_iterations(grid):
    # Initialize a set to store the states of the grid
    states = set()
    
    # Convert the grid to a tuple and add it to the set of states
    states.add(tuple(grid))
    
    # Initialize a counter for the number of iterations
    iterations = 0
    
    # Define the cycle of directions
    directions = ["up", "left", "down", "right"]
    
    # Initialize a variable to store the grid at the moment of the first repetition
    repeated_grid = None
    
    while True:
        
        # Apply the move_os function to the grid in the current direction
        grid = move_Os(grid, directions[iterations % 4])
        
        # Increment the counter
        iterations += 1
        
        # Convert the grid to a tuple
        grid_tuple = tuple(grid)
        
        # If the new state of the grid is already in the set of states
        if grid_tuple in states:
            # If this is the first repetition, store the grid and reset the counter
            if repeated_grid is None:
                repeated_grid = grid_tuple
                cycle_length = 0
            # If this is not the first repetition, and the grid is the same as the grid at the moment of the first repetition, break the loop
            elif grid_tuple == repeated_grid:
                break
        
        # Otherwise, add the new state to the set of states
        states.add(grid_tuple)
        
        # If we have found a repeated state, increment the cycle length counter
        if repeated_grid is not None:
            cycle_length += 1
    
    # Return the number of iterations until the first repetition, the cycle length, and the grid at the moment of the first repetition
    return iterations-cycle_length, cycle_length, grid

def apply_iterations(grid, iterations, cycle_length):
    # Compute the number of additional iterations to apply
    additional_iterations = (4000000000 - (iterations-cycle_length)) % cycle_length
    
    # Define the cycle of directions
    directions = ["up", "left", "down", "right"]
    
    # Apply the Move_Os function 'additional_iterations' times
    for i in range(additional_iterations):
        grid = move_Os(grid, directions[(iterations-cycle_length + i) % 4])
    
    return grid

grid = text.splitlines()
# Get the number of iterations until the first repetition, the cycle length, and the grid at the moment of the first repetition
iterations, cycle_length, new_grid = count_iterations(grid)

# Apply the additional iterations
final_grid = apply_iterations(grid, iterations, cycle_length)

#print(final_grid)
# Now you can apply your calculate_score function to the final grid
score = calculate_score(final_grid)
#print(count_iterations(grid))
print(score)
def apply_exact_iterations(grid, num_iterations):
    # Define the cycle of directions
    directions = ["up", "left", "down", "right"]
    
    # Apply the Move_Os function 'num_iterations' times
    for i in range(num_iterations):
        grid = move_Os(grid, directions[i % 4])
    
    return grid

#print(apply_exact_iterations(grid, 38))