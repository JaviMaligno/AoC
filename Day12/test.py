from C12 import dijkstra, text_to_matrix, multiple_dijkstra
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day12\test.txt") as f: 
    text = f.read()
    grid = text_to_matrix(text)
    #distance = dijkstra(grid)
    min_distance  = multiple_dijkstra(grid)
    print(min_distance)