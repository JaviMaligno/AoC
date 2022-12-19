from C18 import cubes, compute_sides, defaultdict, dfs, original_dfs, get_extremes, non_rec_dfs
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day18\test.txt") as f: 
    text = f.read()
    total, center_dict = compute_sides(text)
    
    coordinates = center_dict.keys()
    rock_points = defaultdict(bool)
    for k in coordinates:
        rock_points[k] = True
    extremes = get_extremes(coordinates)
    min_x, max_x, min_y, max_y, min_z, max_z = extremes
    start = (max_x, max_y, max_z)
    discovered = defaultdict(bool)
    start = (max_x,max_y,max_z)
    print((max_x-min_x)*(max_y-min_y)*(max_z-min_z)) 
    #surface_sides = dfs(start, rock_points)
    #print(surface_sides)
    #print(original_dfs(start, extremes))
    non_rec_dfs(start, extremes, rock_points)