import re
import numpy as np
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(22)

def map_instructions(text):
    lines = text.splitlines()
    width =  len(lines[0])
    for i,line in enumerate(lines):
        if not line:
            break
        lines[i] = line+(' ')*(width - len(line))
    maps = np.array(list(map(list,lines[:i])))
    rocks = np.where(maps == "#", 1, 0)
    instructions = list(map(lambda x: (x[0], int(x[1:])),re.findall("[R|L]?\d+", ''.join(lines[i+1:])))) 
    # I am adding a letter C in front because the first instruction doesn't have any
    instructions[0] = ('C', 30)
    return maps, instructions, rocks

def remove_spaces(index, maps, rocks, col = False):
    if col:
        map_col_blank = maps[:, index]
        rock_col_blank = rocks[:, index]
    else:
        map_col_blank = maps[index ,:] #the name should be map_row but  this way I can avoid code repetition, probably a third name would be better
        rock_col_blank = rocks[index ,:]
    
    frame = [i for i in range(len(map_col_blank)) if map_col_blank[i] in ".#"]
    start = frame[0] #can be optimized being lazy: loop  until reaches "." or "#"
    end = frame[-1]
    map_col = map_col_blank[start:end+1]
    rock_col = rock_col_blank[start:end+1]
    return map_col, rock_col, start


        

        

def move(steps, position,maps, rocks, horizontal = True, dir=1):
    if horizontal:
        pos =  position[1]
        row = position[0]
        map_col, rock_col, start  = remove_spaces(row, maps, rocks)
    else: 
        pos = position[0]
        col = position[1]
        map_col, rock_col, start = remove_spaces(col, maps, rocks, col = True)
        
    col_pos = pos - start
    col_size = len(map_col)
    new_pos = col_pos + dir*steps
    potential_position = new_pos % col_size
    crosses = new_pos // col_size
    if potential_position <= col_pos: 
        if dir < 0:
            left_rocks = [i+1 for i in range(col_pos) if rock_col[i]]#again can be lazy optimized
            if left_rocks:
                col_pos= left_rocks[-1] if crosses else max(potential_position,left_rocks[-1] )
            elif crosses:
                right_rocks = [i+1 for i in range(col_pos+1,col_size) if rock_col[i]]
                if right_rocks:
                    col_pos = max(potential_position,right_rocks[-1]) if right_rocks[-1] < col_size else 0
                else:
                    col_pos = potential_position
            else:
                col_pos = potential_position
                  
        else:
            #there must be crosses in this case case we move to the right and end up on the left
            right_rocks = [i-1 for i in range(col_pos+1,col_size) if rock_col[i]]
            if right_rocks:
                col_pos = right_rocks[0]
            else: 
                left_rocks = [i-1 for i in range(col_pos) if rock_col[i]]
                if left_rocks: # WHEN THERE ARE SEVERAL CLOSED IT WON'T STOP AT THE POTENTIAL_POSITION IF IT HASN'T COMPLETED ALL THE CROSSES
                    if crosses >  1:
                        col_pos = left_rocks[0] if left_rocks[0] >= 0 else col_size-1
                    else:
                        col_pos = min(potential_position, left_rocks[0]) if left_rocks[0] >= 0 else col_size-1
                else:
                    col_pos = potential_position    
    else:
        if dir > 0:
            right_rocks = [i-1 for i in range(col_pos+1,col_size) if rock_col[i]]
            if right_rocks:
                col_pos = right_rocks[0] if crosses else min(right_rocks[0], potential_position)
            elif crosses:
                left_rocks = [i-1 for i in range(col_pos) if rock_col[i]]
                if left_rocks:
                    col_pos = min(potential_position,left_rocks[-1] ) if left_rocks[-1] >=0 else col_size-1
                else:
                    col_pos = potential_position
            else:
                col_pos =  potential_position
        else:
            #there are crosses
            left_rocks = [i+1 for i in range(col_pos) if rock_col[i]]
            if left_rocks:
                col_pos = left_rocks[-1]
            else:
                right_rocks = [i+1 for i in range(col_pos+1,col_size) if rock_col[i]]
                if right_rocks:
                    if crosses > 1:
                        col_pos = right_rocks[-1] if right_rocks[-1] < col_size else 0
                    else:
                        col_pos = max(potential_position,right_rocks[-1]) if right_rocks[-1] < col_size else  0 
                else:
                    col_pos = potential_position
    # i need to translate position in map_col to position in map and viceversa
    pos = col_pos+start 
    if horizontal:
        return (row, pos)
    else:
        return (pos, col)
    

# states (directions) are numbers mod 4, where 0 = right, 1 = down,  2 = left, 3 = up
# This way R is addition by 1 and L is subtraction by 1
def movement(steps, state, position, maps, rocks):
    if state == 0:
        position = move(steps, position, maps, rocks, horizontal = True, dir = 1)
    elif state == 1:
        position = move(steps, position, maps, rocks, horizontal = False, dir = 1)
    elif state == 2:
        position = move(steps, position, maps, rocks, horizontal = True, dir = -1)
    elif state == 3:
        position = move(steps, position, maps, rocks, horizontal = False, dir = -1)

    return position

def path(text, initial_state = 0):
    directions = {'R':1,'L':-1, 'C':0}
    state = initial_state
    maps, instructions, rocks = map_instructions(text)
    cols = maps.shape[1]
    initial_col = min(j for j in range(cols) if maps[0,j] == '.')
    position = (0,initial_col)
    for instruction in instructions:
        state = (state + directions[instruction[0]]) % 4
        position = movement(instruction[1], state, position, maps, rocks)
    return 1000*(position[0]+1) + 4*(position[1]+1) + state

#print(path(text))

# For part 2, subdivide into the 6 faces and define movement to take into account the transition

def faces(maps,rocks):
    map1 = maps[:50, 50:100]
    rock1 = rocks[:50, 50:100]
    map2 = maps[:50, 100:150]
    rock2 = rocks[:50, 100:150]
    map3 = maps[50:100, 50:100]
    rock3 = rocks[50:100, 50:100]
    map4 = maps[100:150, :50]
    rock4 = rocks[100:150, :50]
    map5 = maps[100:150, 50:100]
    rock5 = rocks[100:150, 50:100]
    map6 = maps[150:200, :50]
    rock6 = rocks[150:200, :50]
    map_list = [map1, map2,map3, map4,map5, map6]
    rock_list = [rock1, rock2, rock3, rock4, rock5, rock6]
    return map_list, rock_list

def face_transition(face, state, location):
    if face == 0:
        if state == 0:
            next_face = 1
            next_state = 0
            next_location = location[0], location[1]-49
        elif state == 1:
            next_face = 2
            next_state = 1
            next_location = 49 - location[0], location[1]
        elif state == 2:
            next_face = 3
            next_state = 0
            next_location = 49 - location[0], location[1]
        else:
            next_face = 5
            next_state = 0
            next_location = location[1],location[0]
    elif face == 1:
        if state == 0:
            next_face = 4 
            next_state = 2
            next_location = 49 - location[0], location[1]
        elif state == 1:
            next_face = 2
            next_state = 2
            next_location = location[1], location[0]
        elif state == 2:
            next_face = 0
            next_state = 2
            next_location = location[0], 49 - location[1]
        else:
            next_face = 5
            next_state = 3
            next_location = 49-location[0], location[1]
    elif face == 2:
        if state == 0:
            next_face = 1
            next_state = 3
            next_location = location[1], location[0]
        elif state == 1:
            next_face = 4
            next_state = 1
            next_location = 49 - location[0], location[1]
        elif state == 2:
            next_face = 3
            next_state = 1
            next_location = location[1], location[0]
        else:
            next_face = 0
            next_state = 3
            next_location = 49 - location[0], location[1]
    elif face == 3:
        if state == 0:
            next_face = 4
            next_state = 0
            next_location = location[0], 49 - location[0]
        elif state == 1:
            next_face = 5
            next_state = 1
            next_location = 49 - location[0], location[1]
        elif state == 2:
            next_face = 0
            next_state = 0
            next_location = 49 - location[0], location[1]
        else:
            next_face = 2
            next_state = 0
            next_location = location[1], location[0]
    elif face == 4:
        if state == 0:
            next_face = 1
            next_state = 2
            next_location = 49 - location[0], location[1]
        elif state == 1:
            next_face = 5
            next_state = 2
            next_location = location[1], location[0]
        elif state == 2:
            next_face = 3
            next_state = 2
            next_location = location[0], 49 - location[1]
        else:
            next_face = 2
            next_state = 3
            next_location = 49 - location[0], location[1]
    elif face == 5:
        if state == 0:
            next_face = 4
            next_state = 3
            next_location = location[1], location[0]
        elif state == 1:
            next_face = 1
            next_state = 1
            next_location = 49 - location[0], location[1]
        elif state == 2:
            next_face = 0
            next_state = 1
            next_location = location[1], location[0]
        else:
            next_face = 3
            next_state = 3
            next_location = 49 - location[0], location[1]
    return next_face, next_state, next_location
          



def cube_move(steps, state, position, map_list, rock_list):
    dir = 1 if state < 2 else -1
    vertical = state % 2
    face = position[2]
    row, column = position[0], position[1]
    face_map = map_list[face]
    rock_map = rock_list[face]
    way = face_map[:,column] if vertical else face_map[row, :] 
    way_length = len(way)
    rock_way = rock_map[:,column] if vertical else rock_map[row, :]
    way_position = row if vertical else column
    if dir > 0:
        half_rocks = [i-1 for i in range(way_position+1, way_length) if rock_way[i]]
        half_way = way[way_position+1:]
    else:
        half_way = way[:way_position]
        half_rocks = [i+1 for i in range(way_position) if rock_way[i]][::-1] #so that the first rock I encounter is the first element
    half = len(half_way)
    if steps > half:
        if half_rocks: # I am checking dir twice, this code is not efficient
            next_position = half_rocks[0] 
            return ((next_position, column, face), state) if vertical else ((row, next_position, face),state)
        else:
            next_position = way_length-1 if dir > 0 else 0
            location = next_position, column if vertical else row, next_position
            steps -= half
            next_face, next_state, next_location = face_transition(face, state, location)
            next_rock_map = rock_list[next_face]
            if next_rock_map[next_location]:
                return ((next_position, column, face),state) if vertical else ((row, next_position, face),state)
            else:
                # cube_move on the next face
                position = next_location[0], next_location[1], next_face
                return cube_move(steps-1, next_state, position, map_list, rock_list)
    else:
        potential_position = way_position+dir*steps
        if dir > 0:
            next_position = min(potential_position, half_rocks[0]) if half_rocks else potential_position
        else:
            next_position = max(potential_position, half_rocks[0]) if half_rocks else potential_position
        position = (next_position, column, face) if vertical else (row, next_position, face)
        return position, state
        
        


""" def cube_movement(steps, state, position, map_list,  rock_list):
    if state == 0:
        position = cube_move(steps, position, map_list, rock_list, horizontal = True, dir = 1)
    elif state == 1:
        position = cube_move(steps, position, map_list, rock_list, horizontal = False, dir = 1)
    elif state == 2:
        position = cube_move(steps, position, map_list, rock_list, horizontal = True, dir = -1)
    elif state == 3:
        position = cube_move(steps, position, map_list, rock_list, horizontal = False, dir = -1) """

def compute_position(position):
    face_row = position[0]
    face_column = position[1]
    face = position[2]
    if face == 0:
        face_column += 50
    elif face == 1:
        face_column += 100
    elif face == 2:
        face_column += 50
        face_row +=50
    elif face == 3:
        face_row += 100
    elif face == 4:
        face_row += 100
        face_column += 50
    else:
        face_row += 150
    return face_row+1, face_column+1    
    


def cube_path(text):
    directions = {'R':1,'L':-1, 'C':0}
    state = 0
    maps, instructions, rocks = map_instructions(text)
    map_list,rock_list = faces(maps, rocks)
    position = (0,0,0)
    for instruction in instructions:
        state = (state + directions[instruction[0]]) % 4
        position, state = cube_move(instruction[1], state, position, map_list, rock_list)
    row,column = compute_position(position)
    return 1000*row + 4*column + state


print(cube_path(text))
