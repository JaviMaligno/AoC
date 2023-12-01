import numpy as np
import re
from operator import itemgetter
from collections import defaultdict
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(15)
""" I have thought of 2 approaches:
1. generate all the points covered by each sensor on the given row, adding them to a set to avoid repetition (the set can be built at the end from a list)
2. generate only the boundaries that cut the row to check the extremes and then loop through the row checking distances
The second approach is much faster as it doesn't need to loop through so many points"""

#print(int(re.search('x=\d+, y=\d+',list(map(lambda x:x.split(': '), text.splitlines()))[0][1]).group().split(', ')[0][2:]))
#print(re.search('x=\d+, y=\d+',list(map(lambda x: x.split(': '),text.splitlines()))[0][1]).group())
def manhattan(x:tuple,y:tuple)->float:
    x = np.array(x)
    y = np.array(y)
    distance = np.abs(x-y).sum()
    return distance

# print(manhattan((0,0), (-1,2)))
def get_coordinates(text):
    sensor_distance = {}
    beacons = defaultdict(bool)
    information = list(map(lambda x:x.split(': '), text.splitlines()))
    for info in information:
        sensor_info = re.search('x=\d+, y=\d+',info[0]).group().split(', ')
        sensor_coordinates = int(sensor_info[0][2:]), int(sensor_info[1][2:])
        beacon_info =  re.search('x=-?\d+, y=-?\d+',info[1]).group().split(', ')
        beacon_coordinates = int(beacon_info[0][2:]), int(beacon_info[1][2:])
        distance = manhattan(sensor_coordinates,beacon_coordinates)
        sensor_distance[sensor_coordinates] = distance
        beacons[beacon_coordinates] = True
    return sensor_distance, beacons



# Approach number 1
def cover_all(min_max,row_length = 4000000):
    ordered = sorted(min_max)
    #if ordered[0][0] > 0:
     #   return 0
    #if ordered[-1][1] < row_length:
     #   return row_length
    current = ordered[0]
    for i in range(1,len(ordered)):
        if current[1] >= ordered[i][1]:
            continue
        elif current[1] +1 < ordered[i][0]:
            return current[1] +1
        else:
            current = ordered[i]
    # for (_,ma1),(mi2,_) in zip(ordered[:-1],ordered[1:]):
    #     if ma1+1 < mi2:
    #         return ma1+1
    return None



def row_points(sensor_distance, beacons, row = 2000000, column_limits = 4000000): 
    #visited = dict(zip([(i,row) for i  in range(column_limits+1)], [False].copy()*(column_limits+1)))
    row_points = set()
    #all_points = column_limits+1
    #current_min = column_limits
    #current_max = 0
    min_max = []
    for (sx,sy),d in sensor_distance.items():
        row_distance = abs(sy-row)
        dif = d - row_distance
        #knwon_beacons = len(beacon for beacon in beacons.keys() if beacon[0] == row)
        if dif >= 0 :  
            max_coordinate = min(column_limits, sx+dif)
            min_coordinate = max(0, sx-dif)
            if min_coordinate <= max_coordinate:
                min_max.append((min_coordinate, max_coordinate))
            #current_max = max_coordinate if max_coordinate > current_max else current_max
            #current_min = min_coordinate if min_coordinate < current_min else current_min
            #points = [y for i in range(min_coordinate, max_coordinate+1) if (not beacons[(y:=(i, row))])  ] # For first part only
            #row_points.update([(i,row) for i in range(min_coordinate,max_coordinate+1)])
            """ for  i in range(min_coordinate, max_coordinate+1):
                    if (not beacons[(i, row)]):
                        row_points.add((i,row)) 
                        
                    else:
                        pass
                    all_points.add((i,row)) """
            """ elif dif == 0:
            point = (sx, row)
            if beacons[point] or not(0 <= sx <= column_limits):
                continue
            else:
                row_points.add(point) """
    
    #row_points
    index= cover_all(min_max, row_length = column_limits)
    return False if index is None else index
    #return min_max
    #return len(row_points)
        
     
def no_beacon_1(text, row_limit = 4000000, row = False):
    sensors, beacons = get_coordinates(text)
    #all_row = row_limit +1 
    if row:
        beacon = row_points(sensors, beacons, row = row, column_limits=row_limit)
        return beacon
    for i in range(row_limit+1):
        beacon = row_points(sensors, beacons, row = i, column_limits=row_limit)
        if beacon:
            return i+row_limit*beacon
        else:
            continue
    return beacon

print(no_beacon_1(text)) #the solution is the whole fucking row
# Approach number 2
def row_exremes(sensor_distance, row = 2000000):
    cuts = []
    # I could store the ones that give a small distance so that I don't check extra times, but there are not many
    for (sx,sy),d in sensor_distance.items():
        row_distance = abs(sy-row)
        dif = d - row_distance
        if dif > 0 :  
            cut = [(sx+dif,row), (sx-dif,row)]
            cuts.extend(cut)
        elif dif == 0:
            cut = (sx, row)
            cuts.append(cut)
        else:
            continue
    min_cut, max_cut = min(cuts,key=itemgetter(0))[0], max(cuts, key=itemgetter(0))[0]
    return min_cut, max_cut

""" sensors,_ = get_coordinates(text)
min_cut, max_cut = row_exremes(sensors)
print(-min_cut,max_cut) """

def no_beacon_2(text, row = 2000000):
    sensors, beacons = get_coordinates(text)
    min_cut, max_cut = row_exremes(sensors, row=row)
    no_beacon = 0
    for i in range(min_cut, max_cut+1):
        no_beacon = no_beacon + 1 if (not beacons[i,row]) and (any(manhattan((i,row), s)<=d for s,d in sensors.items())) else no_beacon
    return no_beacon



