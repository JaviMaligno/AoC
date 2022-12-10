import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(9)
import numpy as np

def motion_list(text, one_step = False):
    motions = list(map(lambda x: (x.split(' ')[0], int(x.split(' ')[1])), text.splitlines()))
    if one_step:
        one_step_motions = []
        for (x,y) in motions:
            one_step_motions.extend([(x,1) for i in range(y)])
        motions = one_step_motions
    return motions
motions = motion_list(text, one_step=True)
print(motions[0])
S = np.array([0,0])
H = S.copy()
T = S.copy()
#visited = {tuple(S)}
#visited_amount = 1
tails = [T.copy() for i in range(9)]




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
    
def diagonal_move(mark, horizontal, vertical, count = False, visited = {}):
    if count:
        mark += np.array([horizontal, vertical])
        visited.add(tuple(mark))
    else:
        mark += np.array([horizontal, vertical])
    return mark, visited

#print(diagonal_move(H, 1,1, visited = visited))
    
def move(mark, mode, *args, **kwargs):
    if mode == "s":
        return straight_move(mark, *args, **kwargs)
    elif mode == "d":
        return diagonal_move(mark, *args, **kwargs)
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
            direction = "U"
        else:
            direction = "D"
               
    elif head[1] == tail[1]:
        diff = head[0] - tail[0]
        if diff > 0:
            direction = "R"
        else:
            direction = "L"
    else: 
        return False
    return direction, abs(diff)-1
    
def update_chain(chain, i, head, tail):
    chain[i] = (head,tail)
    try:
        chain[i+1][0] = tail
    except:
        pass
def movements(head, tails,visited):
    whole_chain = [head,*tails]
    chain = list(map(list,zip([head,*tails[:-1]], tails)))
    for i, [current_head, tail] in enumerate(chain):
        while not touching(current_head, tail):
            if same_row_or_column(current_head, tail):
                direction, steps = same_row_or_column(current_head, tail)
                if i == len(chain)-1:
                    tail, visited = move(tail, "s", direction, steps, count = True, visited = visited)
                else:
                    tail, _ = move(tail, "s", direction, steps)
            else:
                if current_head[0] == tail[0] + 1:
                    diff = current_head[1] - tail[1]
                    vertical = diff//abs(diff)
                    horizontal = 1
                elif current_head[0] == tail[0] - 1:
                    diff = current_head[1] - tail[1]
                    vertical = diff//abs(diff)
                    horizontal = -1
                elif current_head[1] == tail[1] + 1:
                    diff = current_head[0] - tail[0]
                    vertical = 1
                    horizontal = diff//abs(diff)
                elif head[1] == tail[1] - 1:
                    diff = current_head[0] - tail[0]
                    vertical = -1
                    horizontal = diff//abs(diff)
                else:
                    hor_diff = current_head[0] - tail[0]
                    ver_dif = current_head[1] - tail[1]
                    horizontal = hor_diff//abs(hor_diff)
                    vertical = ver_dif//abs(ver_dif)
                if i == len(chain)-1:
                    tail, visited = move(tail, "d", horizontal, vertical, count = True, visited = visited)
                else:
                    tail, _ = move(tail, "d", horizontal, vertical)
        update_chain(chain,i,current_head,tail)
        """     if touching(current_head, tail):
                    update_chain(chain,i,current_head,tail)
                    continue
                else: 
                    direction, steps = same_row_or_column(current_head, tail)
                    tail, visited = move(tail, "s", direction, steps, count = True, visited = visited)
                    update_chain(chain,i,current_head,tail) """


def visited_positions(head, tails, start, motions):
    visited = {tuple(start)}
    
    for motion in motions:
        head,_ = move(head, "s", *motion)
        movements(head, tails, visited)
        
    return visited
                


        
    


visited = visited_positions(H, tails, S, motions)

print(len(visited))