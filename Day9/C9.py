import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(9)
import numpy as np


motions = list(map(lambda x: (x.split(' ')[0], int(x.split(' ')[1])), text.splitlines()))
print(motions[0])
S = np.array([0,0])
H = S.copy()
T = S.copy()
visited = {tuple(S)}
visited_amount = 1





def straight_move(mark: np.ndarray(shape=(1,2)), direction: str, steps: int, count = False, visited = {}):
    if direction == "L":
        movement = np.array([-1,0])
    elif direction == "R":
        movement = np.array([1,0])
    elif direction == "U":
        movement = np.array([0,1])
    elif direction == "D":
        movement = np.array([0,-1])
    if count:
        for i in range(1,steps+1):
            mark += movement
            visited.add(tuple(mark)) # There is no need to store the visited positions, but I want to do it
    else:
        mark += steps*movement
    return mark, visited

#print(straight_move(H, *motions[0], count = True, visited = visited))
    
def diagonal_move(mark, horizontal, vertical, visited):
    mark += np.array([horizontal, vertical])
    visited.add(tuple(mark))
    return mark, visited

#print(diagonal_move(H, 1,1, visited = visited))
    
def move(mark, mode, *args, **kwargs):
    if mode == "s":
        return straight_move(mark, *args, **kwargs)
    elif mode == "d":
        return diagonal_move(mark, *args)
# =============================================================================
# print(T)
# ex1, _ = move(H, "s", *motions[0], count = True, visited = visited)
# print(T)
# ex2, _ = move(T, "d", -1,1,visited )
# print(T)
# print(ex1)
# print(ex2)
# =============================================================================

def touching(head: np.ndarray(shape=(1,2)), tail: np.ndarray(shape=(1,2))) -> bool:
    pseudo_distance = np.absolute(head - tail).max()
    touching = pseudo_distance <= 1
    return touching

#print(touching(ex1,ex2))

def same_row_or_column(head, tail):
    if head[0] == tail[0]:
        diff = head[1] - tail[1]
        if diff > 0:
            direction = "R"
        else:
            direction = "L"
               
    elif head[1] == tail[1]:
            diff = head[0] - tail[0]
            if diff > 0:
                direction = "U"
            else:
                direction = "D"
    else: 
        return False
    return direction, diff-1
    

def visited_positions(head, tail, start, motions):
    visited = {tuple(start)}
    for motion in motions:
        head,_ = move(head, "s", *motion)
        if touching(head, tail):
            continue
        else:
            if same_row_or_column(head, tail):
                direction, steps = same_row_or_column(head, tail)
                tail, visited = move(tail, "s", direction, steps, count = True, visited = visited)
            else:
                if head[0] == tail[0] + 1:
                    diff = head[1] - tail[1]
                    horizontal = (diff - 1)//abs(diff-1)
                    vertical = 1
                elif head[0] == tail[0] - 1:
                    diff = head[1] - tail[1]
                    horizontal = (diff - 1)//abs(diff-1)
                    vertical = -1
                elif head[1] == tail[1] + 1:
                    diff = head[0] - tail[0]
                    horizontal = 1
                    vertical = (diff - 1)//abs(diff-1)
                elif head[1] == tail[1] - 1:
                    diff = head[0] - tail[0]
                    horizontal = -1
                    vertical = (diff - 1)//abs(diff-1)

                tail, visited = move(tail, "d", horizontal, vertical, visited)
                steps, direction = same_row_or_column(head, tail)
                tail, visited = move(tail, "s", direction, steps, count = True, visited = visited)
    return visited
                


        
    


visited = visited_positions(H, T, S, motions)

print(visited)