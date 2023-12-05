import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(5)

"""
Inefficient

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

    return seeds, maps """
 
# def parse_input(input_string):
#     lines = input_string.splitlines()
#     seeds = list(map(int, lines[0].split(':')[1].strip().split()))
#     maps = {}
#     current_map = None
#     for line in lines[1:]:
#         if 'map:' in line:
#             current_map = line.split(':')[0]
#             maps[current_map] = []
#         elif line:
#             maps[current_map].append(list(map(int, line.split())))
#     return seeds, maps

def parse_input(input_text):
    lines = input_text.splitlines()
    seeds = list(map(int, lines[0].split(':')[1].strip().split()))
    maps = {}
    current_map = None
    for line in lines[1:]:
        if 'map:' in line:
            current_map = line.split(':')[0]
            maps[current_map] = []
        elif line:
            maps[current_map].append(list(map(int, line.split())))
    return seeds, maps

def find_location(seed, maps):
    current_value = seed
    for map_name in ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map', 'humidity-to-location map']:
        current_map = maps[map_name]
        for dest_start, src_start, length in current_map:
            if src_start <= current_value < src_start + length:
                current_value = dest_start + (current_value - src_start)
                break
    return current_value


def lowest_location(seeds, maps):
    # Find the location for each seed
    locations = [find_location(seed, maps) for seed in seeds]

    # Find the lowest location
    lowest_location = min(locations)

    return lowest_location

""" 
Inefficient

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
 """
#seeds, maps = parse_input(text)
#print(lowest_location(seeds, maps))

def parse_input2(input_text):
    lines = input_text.split('\n')
    seed_ranges = list(map(int, lines[0].split(':')[1].strip().split()))
    seeds = [(seed_ranges[i], seed_ranges[i+1]) for i in range(0, len(seed_ranges), 2)]
    maps = {}
    current_map = None
    for line in lines[1:]:
        if 'map:' in line:
            current_map = line.split(':')[0] 
            maps[current_map] = []
        elif line:
            maps[current_map].append(list(map(int, line.split())))
    return seeds, maps

def find_location2(seed_ranges, maps):
    min_location = float('inf')
    for seed_start, seed_length in seed_ranges:
        for seed in range(seed_start, seed_start + seed_length):
            current_value = seed
            for map_name in ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map', 'humidity-to-location map']:
                current_map = maps[map_name]
                for dest_start, src_start, length in current_map:
                    if src_start <= current_value < src_start + length:
                        current_value = dest_start + (current_value - src_start)
                        break
            min_location = min(min_location, current_value)
    return min_location


seeds, maps = parse_input2(text)
#print(find_location2(seeds, maps))
print(seeds)