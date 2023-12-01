from C14 import lines, set_rocks, count_rest, floor
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day14\test.txt") as f: 
    text = f.read()
    instructions = lines(text)
    rocks = set_rocks(instructions)
    rest = count_rest(rocks)
    #print(floor(rocks))
    print(rest)