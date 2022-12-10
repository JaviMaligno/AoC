from C9 import motion_list, visited_positions, S, H, tails
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day9\test.txt") as f: 
    text = f.read()
    motions = motion_list(text, one_step=True)
    visited = visited_positions(H,tails, S, motions)
    print(visited)
    print(len(visited))