import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(3)


def sum_part_numbers(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')

    # Initialize an empty list to store the part numbers
    part_numbers = []

    # Initialize an empty set to store the locations that have been counted
    counted_locations = set()

    # Iterate over each cell in the grid
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # If the cell contains a symbol
            if not lines[i][j].isdigit() and lines[i][j] != '.':
                # Check all 8 directions around the symbol
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    x, y = i + dx, j + dy
                    # If the adjacent cell is within the grid and contains a digit
                    if 0 <= x < len(lines) and 0 <= y < len(lines[x]) and lines[x][y].isdigit():
                        # Find the whole number that the digit belongs to
                        start, end = y, y
                        while start - 1 >= 0 and lines[x][start - 1].isdigit():
                            start -= 1
                        while end + 1 < len(lines[x]) and lines[x][end + 1].isdigit():
                            end += 1
                        # If the location has not been counted yet
                        if (x, start) not in counted_locations:
                            # Add the number to the list of part numbers
                            part_numbers.append(int(lines[x][start:end+1]))
                            # Add the location to the set of counted locations
                            counted_locations.add((x, start))

    # Return the sum of the part numbers
    return sum(part_numbers)

def sum_gear_ratios(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')

    # Initialize an empty list to store the part numbers
    part_numbers = {}

    # Initialize an empty set to store the locations that have been counted
    counted_locations = set()

    # Iterate over each cell in the grid
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # If the cell contains a symbol
            if not lines[i][j].isdigit() and lines[i][j] != '.':
                # Check all 8 directions around the symbol
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    x, y = i + dx, j + dy
                    # If the adjacent cell is within the grid and contains a digit
                    if 0 <= x < len(lines) and 0 <= y < len(lines[x]) and lines[x][y].isdigit():
                        # Find the whole number that the digit belongs to
                        start, end = y, y
                        while start - 1 >= 0 and lines[x][start - 1].isdigit():
                            start -= 1
                        while end + 1 < len(lines[x]) and lines[x][end + 1].isdigit():
                            end += 1
                        # If the location has not been counted yet
                        if (x, start) not in counted_locations:
                            # Add the number to the list of part numbers
                            part_number = int(lines[x][start:end+1])
                            part_numbers.setdefault((i, j), []).append(part_number)
                            # Add the location to the set of counted locations
                            counted_locations.add((x, start))

    # Calculate the gear ratios
    gear_ratios = [pn[0] * pn[1] for pn in part_numbers.values() if len(pn) == 2]

    # Return the sum of the gear ratios
    return sum(gear_ratios)



print(sum_gear_ratios(text))





#print(sum_part_numbers(text))  






