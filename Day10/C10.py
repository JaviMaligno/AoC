import numpy as np
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(10)
def get_commands(text):
        commands = list(map(lambda x: x.split(' '), text.splitlines()))
        return commands

commands= get_commands(text)
check_points = [20,60,100,140,180,220] # could be defined more  generally but there is no need

X = 1


def compute_strength(cycle, check_points, strength, X):
    if cycle in check_points:
        strength += cycle * X
    return strength

def strength(commands, X, check_points):
    strength = 0
    cycle = 0
    for command in commands:
        if len(command) == 1:
            cycle += 1
            strength = compute_strength(cycle, check_points, strength, X)
        else:
            # I only need to compute one of these in each case really, I may refactor but I think it would make little difference
            cycle += 1
            strength = compute_strength(cycle, check_points,strength,X)
            cycle +=1
            strength = compute_strength(cycle, check_points,strength,X) 
            X += int(command[1])
    return strength #, cycle -> there are 240 cycles

#print(strength(commands, X, check_points))

R = []
rows = [R.copy() for i in range(6)] # could be defined more generally but there is no need

def draw(cycle, crt,sprite, row_index, rows):
    if crt in sprite:
        rows[row_index].append(crt)
    """ if cycle % 40 == 0:
        row_index +=1
        cycle +=1 
        crt = 0   #could use % and // to avoid if statement  
    else:
        cycle += 1
        crt += 1 """
    row_index = cycle // 40
    crt = cycle % 40
    cycle +=1

    return cycle, crt, rows, row_index

def pixels(commands, rows):   
    cycle = 1
    crt = 0 #actually I could just carry the cycle and subtract one for the crt everytime
    row_index = 0
    sprite = np.array([0,1,2]) #Could define it in terms of X but there's no need
    for command in commands:
        if len(command) == 1:
            cycle, crt, rows, row_index = draw(cycle, crt, sprite,row_index, rows)
        else: 
            cycle, crt, rows, row_index = draw(cycle, crt, sprite,row_index, rows)
            cycle, crt, rows, row_index = draw(cycle, crt, sprite,row_index, rows)
            sprite  += int(command[1])
    return rows

def picture(rows): # more generally I could provide the CRT dimensions but there is no need
    for row in rows:
        string = ''.join(["#" if i in row else "." for i in range(40) ])
        print(string)

rows = pixels(commands, rows)
picture(rows)
            
            

            
    