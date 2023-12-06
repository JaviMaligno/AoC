import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(6)

def process_text(text):
    lines = text.split('\n')
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    return list(zip(times, distances))

def count_values(time_distance_pairs):
    product = 1
    for time, distance in time_distance_pairs:
        count = sum(1 for v in range(time+1) if v*(time-v) > distance)
        product *= count
    return product


def concatenate_numbers(text):
    lines = text.split('\n')
    times = ''.join(lines[0].split()[1:])
    distances = ''.join(lines[1].split()[1:])
    return int(times), int(distances)

# Example usage:

time, distance = concatenate_numbers(text)



#pairs = process_text(text)
#print(pairs)
print(count_values([(time,distance)]))