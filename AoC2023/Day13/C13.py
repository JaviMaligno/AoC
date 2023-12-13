import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(13)


def process_patterns(text):
    # Split the text by empty lines
    patterns = text.split('\n\n')

    # Split each pattern into a list of rows
    patterns = [pattern.split('\n') for pattern in patterns]

    return patterns



def find_vertical_reflection(pattern):
    # Convert the pattern to a list of lists for easier manipulation
    pattern = [list(row) for row in pattern]

    # Get the number of rows and columns
    num_rows = len(pattern)
    num_cols = len(pattern[0])

    # Iterate over possible split points
    for split_point in range(1, num_cols):
        # Get the left and right subsets
        left_subset = [row[:split_point] for row in pattern]
        right_subset = [row[split_point:] for row in pattern]

        # Get the sizes of the subsets
        n = len(left_subset[0])
        m = len(right_subset[0])

        # Check for reflection
        if n < m:
            # Check if the left side is a reflection of the first n columns of the right side
            if all(left_subset[i] == right_subset[i][:n][::-1] for i in range(num_rows)):
                return split_point
        else:
            # Check if the right side is a reflection of the last m columns of the left side
            if all(left_subset[i][-m:][::-1] == right_subset[i] for i in range(num_rows)):
                return split_point

    # If no reflection was found, return 0
    return 0



pattern = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.'
]

print(find_vertical_reflection(pattern))  # This will print True or False

def find_horizontal_reflection(pattern):
    # Convert the pattern to a list of lists for easier manipulation
    pattern = [list(row) for row in pattern]

    # Get the number of rows and columns
    num_rows = len(pattern)
    num_cols = len(pattern[0])

    # Iterate over possible split points
    for split_point in range(1, num_rows):
        # Get the top and bottom subsets
        top_subset = pattern[:split_point]
        bottom_subset = pattern[split_point:]

        # Get the sizes of the subsets
        n = len(top_subset)
        m = len(bottom_subset)

        # Check for reflection
        if n < m:
            # Check if the top side is a reflection of the first n rows of the bottom side
            if top_subset == bottom_subset[:n][::-1]:
                return split_point
        else:
            # Check if the bottom side is a reflection of the last m rows of the top side
            if top_subset[-m:][::-1] == bottom_subset:
                return split_point

    # If no reflection was found, return 0
    return 0

pattern = [
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#'
]

print(find_horizontal_reflection(pattern))  # This will print the number of rows in the top pattern or 0


def process_and_score_patterns(text):
    # Process the text to get the list of patterns
    patterns = process_patterns(text)

    # Initialize the total score
    total_score = 0

    # Loop through the patterns
    for pattern in patterns:
        # Apply the find_vertical_reflection and find_horizontal_reflection functions
        vertical_score = find_vertical_reflection(pattern)
        horizontal_score = find_horizontal_reflection(pattern)

        # Add the scores to the total score
        total_score += vertical_score + 100 * horizontal_score

    # Return the total score
    return total_score

print(process_and_score_patterns(text))  # This will print the total score


def find_almost_vertical_reflection(pattern):
    pattern = [list(row) for row in pattern]

    for split_point in range(1, len(pattern[0])):
        left_subset = [row[:split_point] for row in pattern]
        right_subset = [row[split_point:] for row in pattern]

        n = len(left_subset[0])
        m = len(right_subset[0])

        if n < m:
            differences = sum(a != b for row_left, row_right in zip(left_subset, right_subset) for a, b in zip(row_left, row_right[:n][::-1]))
            if differences == 1:
                return split_point
        else:
            differences = sum(a != b for row_left, row_right in zip(left_subset, right_subset) for a, b in zip(row_left[-m:][::-1], row_right))
            if differences == 1:
                return split_point

    return 0


def find_almost_horizontal_reflection(pattern):
    pattern = [list(row) for row in pattern]

    for split_point in range(1, len(pattern)):
        top_subset = pattern[:split_point]
        bottom_subset = pattern[split_point:]

        n = len(top_subset)
        m = len(bottom_subset)

        if n < m:
            # Flatten the rows and compare individual cells
            differences = sum(a != b for row_top, row_bottom in zip(top_subset, bottom_subset[:n][::-1]) for a, b in zip(row_top, row_bottom))
            if differences == 1:
                return split_point
        else:
            # Flatten the rows and compare individual cells
            differences = sum(a != b for row_top, row_bottom in zip(top_subset[-m:][::-1], bottom_subset) for a, b in zip(row_top, row_bottom))
            if differences == 1:
                return split_point

    return 0





pattern = [
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#'
]

pattern = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.'
]

print(find_almost_vertical_reflection(pattern))  # This will print the number of columns on the left side of the reflection or 0
print(find_almost_horizontal_reflection(pattern))  # This will print the number of rows in the top pattern or 0

def process_and_score_almost_patterns(text):
    # Process the text to get the list of patterns
    patterns = process_patterns(text)

    # Initialize the total score
    total_score = 0

    # Loop through the patterns
    for pattern in patterns:
        # Apply the find_almost_vertical_reflection function
        vertical_score = find_almost_vertical_reflection(pattern)
        
        if vertical_score > 0:
            # If an almost vertical reflection is found, add its score to the total score
            total_score += vertical_score
        else:
            # If no almost vertical reflection is found, apply the find_almost_horizontal_reflection function
            horizontal_score = find_almost_horizontal_reflection(pattern)
            
            # Add the horizontal score (multiplied by 100) to the total score
            total_score += 100 * horizontal_score

    # Return the total score
    return total_score

print(process_and_score_almost_patterns(text))