from collections import defaultdict
from operator import itemgetter
import numpy as np
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
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

points = center_dict.keys()

max_x = max(points)
min_x = min(points)
max_y = max(points, key = itemgetter(1))
min_y = min(points, key = itemgetter(1))
max_z = min(points, key = itemgetter(2))
min_z = min(points, key = itemgetter(2))


