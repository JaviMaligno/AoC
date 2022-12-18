from C18 import cubes, compute_sides
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day18\test.txt") as f: 
    text = f.read()
    center_list = cubes(text)
    print(compute_sides(center_list))
    