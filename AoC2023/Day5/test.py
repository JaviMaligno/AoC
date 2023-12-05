from C5 import *
with open(r"AoC2023\Day5\test.txt") as f: 
    text = f.read()
    seeds, maps = parse_input2(text)
    print(find_location2(seeds, maps))