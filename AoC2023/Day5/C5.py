import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(5)

def parse_input(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')

    # Initialize an empty dictionary to hold the maps
    maps = {}

    # Initialize an empty list to hold the current map
    current_map = []

    # Initialize an empty list to hold the seeds
    seeds = []

    # Iterate over the lines
    for line in lines:
        # If the line is empty, skip it
        if not line.strip():
            continue

        # If the line starts with "seeds:", it's the list of seeds
        if line.startswith('seeds:'):
            seeds = list(map(int, line[7:].split()))
            continue

        # If the line ends with "map:", it's the start of a new map
        if line.endswith('map:'):
            # If there's a current map, add it to the maps
            if current_map:
                maps[current_map[0]] = current_map[1]

            # Start a new map with the name of the map as the key
            current_map = [line[:-5], {}]

        # If the line contains numbers, it's part of the current map
        elif ' ' in line:
            # Split the line into destination range start, source range start, and range length
            dest_start, src_start, length = map(int, line.split())

            # Add the source and destination values to the current map
            for i in range(length):
                current_map[1][src_start + i] = dest_start + i

    # Add the last map to the maps
    if current_map:
        maps[current_map[0]] = current_map[1]

    return seeds, maps


def find_locations(seeds, maps):
    # Initialize an empty list to hold the locations
    locations = []

    # Iterate over the seeds
    for seed in seeds:
        # Start with the seed
        current_value = seed

        # Traverse the maps
        for map_name in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
            # Get the current map
            current_map = maps[map_name]

            # If the current value is in the map, update it
            if current_value in current_map:
                current_value = current_map[current_value]

        # Add the final location to the list
        locations.append(current_value)

    # Return the lowest location
    return min(locations)

seeds, maps = parse_input(text)
print(find_locations(seeds, maps))