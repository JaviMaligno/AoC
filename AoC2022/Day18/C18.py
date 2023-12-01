from collections import defaultdict
from operator import itemgetter
import numpy as np
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
sys.setrecursionlimit(100000)
from get_data import get_input
text = get_input(18)
#print(text)
#text = open("input.txt").read()
def default_value():
    return 6

def cubes(text):
    centers = list(map(lambda x: tuple(map(int,x.split(','))), text.splitlines()))
    return centers

def adjacent(cube1,cube2):
    return sum(abs(x-y) for x,y in zip(cube1,cube2)) == 1

def compute_sides(text):
    centers = cubes(text)
    total = len(centers)*6
    center_dict = defaultdict(default_value)
    for i, cube1 in enumerate(centers):
        if center_dict[cube1] == 0:
            continue
        for cube2 in centers[i+1:]:
            if center_dict[cube2] == 0:
                continue
            if adjacent(cube1,cube2):
                center_dict[cube1] -= 1
                center_dict[cube2] -= 1
                total -= 2
            if center_dict[cube1] == 0:
                break
    return total, center_dict


total, center_dict = compute_sides(text)
coordinates = center_dict.keys()
def rock(coordinates):
    rock_points = defaultdict(bool)
    for k in coordinates:
        rock_points[k] = True
    return rock_points
#print(rock(coordinates))
# I add and substract 1 because I will use the exterior to detect the surface
def get_extremes(coordinates):
    max_x = max(coordinates)[0]+1
    min_x = min(coordinates)[0]-1
    max_y = max(coordinates, key = itemgetter(1))[1]+1
    min_y = min(coordinates, key = itemgetter(1))[1]-1
    max_z = max(coordinates, key = itemgetter(2))[2]+1
    min_z = min(coordinates, key = itemgetter(2))[2]-1
    extremes = (min_x, max_x, min_y, max_y, min_z, max_z)
    return extremes
def adjacents(point, extremes):
    min_x, max_x, min_y, max_y, min_z, max_z = extremes
    x,y,z = point
    adjacents = []
    if min_x < x:
        adjacents.append((x-1,y,z))
    if x < max_x:
        adjacents.append((x+1,y,z))
    if min_y < y:
        adjacents.append((x,y-1, z))
    if y < max_y:
        adjacents.append((x,y+1,z))
    if min_z < z:
        adjacents.append((x,y,z-1))
    if z < max_z:
        adjacents.append((x,y,z+1))
    return adjacents


#print(adjacents(start))
extremes = get_extremes(coordinates)
def dfs(start, extremes, rock_points, sides = 0, discovered = defaultdict(bool)):
    sides = sides
    discovered = discovered
    if rock_points[start]:
        sides +=1
    else:
        discovered[start] = True
    
    adjacent_cubes = adjacents(start, extremes)
    for cube in adjacent_cubes:
        if rock_points[cube]:
            sides += 1
            continue
        if not discovered[cube]:
            sides += dfs(cube, rock_points, sides = sides, discovered= discovered) 
    return sides

#surface_sides = dfs(start, rock_points)
#print(surface_sides)

#print(max_x,max_y, max_z, min_x,min_y, min_z)
discovered = defaultdict(bool)

def original_dfs(start, extremes):
    if not discovered[start]:
        print(start)
        discovered[start] = True
        adjacent_cubes = adjacents(start, extremes)
        for cube in adjacent_cubes:
            if not discovered[cube]:
                original_dfs(cube, extremes)
    return discovered
min_x, max_x, min_y, max_y, min_z, max_z = extremes
start = (max_x, max_y, max_z)
#print(original_dfs(start,extremes))
rock_points = rock(coordinates)
discover = 0
def dev_dfs(start, extremes, rock_points, discover = 0):
    if not discovered[start]:
        discovered[start] = True if not rock_points[start] else False
        discover = discover +1 if rock_points[start] else discover
        print(start, discovered[start], discover)
        adjacent_cubes = adjacents(start, extremes)
        for cube in adjacent_cubes:
            if not discovered[cube] and not rock_points[cube]:
                dev_dfs(cube, extremes, rock_points, discover = discover)
    return discovered
#print(dev_dfs(start,extremes, rock_points))

def non_rec_dfs(start, extremes, rock_points, stack = [], sides = 0):
    stack.append(start)
    while stack:
        v =  stack.pop()
        if not discovered[v]:
            discovered[v] = True
            adjacent_cubes = adjacents(v, extremes)
            print(v, adjacent_cubes)
            for cube in adjacent_cubes:
                if rock_points[cube]:
                    sides += 1
                    print(cube, "SIDE", sides)
                    continue
                elif not discovered[cube]:
                    stack.append(cube)
                    
    return sides
non_rec_dfs(start, extremes, rock_points)



