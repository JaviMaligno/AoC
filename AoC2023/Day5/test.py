from C5 import *
with open(r"AoC2023\Day5\test.txt") as f: 
    text = f.read()
    seeds, maps = parse_input(text)
    print(find_locations(seeds, maps))