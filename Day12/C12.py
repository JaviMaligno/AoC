import numpy as np
import pandas as pd
from string import ascii_lowercase
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(12)
letter_values = dict(zip(ascii_lowercase, range(len(ascii_lowercase))))
letter_values.update({'S':0, 'E':25})
# print(letter_values)
INF = np.inf
def text_to_matrix(text):
    grid = np.array(list(map(list,text.splitlines())))
    return grid

def start_end(grid):
    START = np.where(grid == 'S')[0][0], np.where(grid == 'S')[1][0]
    END = np.where(grid == 'E')[0][0], np.where(grid == 'E')[1][0]
    return START, END
def get_nodes(grid):
    return list(map(lambda x: x[0], np.ndenumerate(grid))) 


def adjacent_vertices(vertex_row,vertex_column, grid):
    shape = grid.shape
    position = (vertex_row, vertex_column)
    vertex = grid[vertex_row,vertex_column]
    if position == (0,0):
        down = vertex_row+1,vertex_column
        right = vertex_row,vertex_column+1
        candidates = [down, right]
    elif position == (0, shape[1]-1):
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        candidates = [down, left]
    elif position == (shape[0]-1, 0):
        up = vertex_row-1,vertex_column
        right = vertex_row,vertex_column+1
        candidates = [up, right]
    elif position == (shape[0]-1,shape[1]-1):
        up = vertex_row-1,vertex_column
        left =  vertex_row,vertex_column-1
        candidates = [up, left]
    elif position[0] == 0:
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        right = vertex_row,vertex_column+1
        candidates = [down,left, right]
    elif position[0] == shape[0]-1:
        up = vertex_row-1,vertex_column
        left =  vertex_row,vertex_column-1
        right = vertex_row,vertex_column+1
        candidates = [up, left, right]
    elif position[1] == 0:
        up = vertex_row-1,vertex_column
        down = vertex_row+1,vertex_column
        right = vertex_row,vertex_column+1
        candidates = [up,down, right]
    elif position[1] == shape[1]-1:
        up = vertex_row-1,vertex_column
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        candidates = [up, down, left]
    else:
        up = vertex_row-1,vertex_column
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        right = vertex_row,vertex_column+1
        candidates = [up, down, left, right]
        
    adjacents = [candidate for candidate in candidates if letter_values[grid[candidate]] <= letter_values[vertex] +1 ]   
    return set(adjacents)


def adjacency_dict(grid,nodes):
    adjacency_dict = {}
    for node in nodes:
        vertex_row = node[0]
        vertex_column = node[1]
        adjacents = adjacent_vertices(vertex_row, vertex_column, grid)
        adjacency_dict[node] = adjacents
    return adjacency_dict

def initial_lengths(nodes, start):
    initial_lengths = {}
    for node in nodes:
        initial_lengths[node] = np.inf
    initial_lengths[start] = 0
    return initial_lengths
    
""" grid = text_to_matrix(text)
nodes = get_nodes(grid)
init_lengths = initial_lengths(nodes, start)
adjacency = adjacency_dict(grid, nodes)
START, END = start_end(grid)
init_lengths = initial_lengths(nodes, START)
 """
def dijkstra(grid, start = None):
    if not start:
        start, end = start_end(grid)
    else:
        _,end = start_end(grid)
    nodes = get_nodes(grid)
    adjacency = adjacency_dict(grid, nodes)
    lengths = initial_lengths(nodes, start)
    unvisited_nodes = set(nodes)
    #unvisited_nodes = grid*True # more efficient if I create a map or array inn which map[node] = True if (un)visited and false otherwise
    # this requires changing the while. Using any will be just as slow. 
    # Use a priority queue instead
    while unvisited_nodes:
        current_dict = {node : length for node, length in lengths.items()  if node in unvisited_nodes}
        current_node = min(current_dict, key = current_dict.get)
        unvisited_nodes.discard(current_node)
        if current_node == end:
            break
        for neighbor in adjacency[current_node].intersection(unvisited_nodes):
            tentative_distance = lengths[current_node] + 1
            if tentative_distance < lengths[neighbor]:
                lengths[neighbor] = tentative_distance
        
    return lengths[end]

grid = text_to_matrix(text)
#print(dijkstra(grid))
def starts(grid):
    # my input has the particularity that any reachable starting point is on the leftmost column
    # except a few that require going to the left anyway
    return [(i,0) for i in range(grid.shape[0]) if grid[i,0] == 'a' or grid[i,0] == 'S']

def multiple_dijkstra(grid):
    start_list = starts(grid)
    return min([dijkstra(grid, start) for start in start_list])

print(multiple_dijkstra(grid))

# no necessary from here

def filter_candidates(vertex_row, vertex_column, candidates):
    filtered = list(filter(lambda x: x[0] > vertex_row or x[1] > vertex_column, candidates))
    return filtered

# a version for the adjacency matrix
def filtered_adjacent_vertices(vertex_row,vertex_column, grid):
    shape = grid.shape
    position = (vertex_row, vertex_column)
    vertex = grid[vertex_row,vertex_column]
    if position == (0,0):
        down = vertex_row+1,vertex_column
        right = vertex_row,vertex_column+1
        candidates = filter_candidates(vertex_row, vertex_column,[down, right])
    elif position == (0, shape[1]-1):
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        candidates = filter_candidates(vertex_row, vertex_column,[down, left])
    elif position == (shape[0]-1, 0):
        up = vertex_row-1,vertex_column
        right = vertex_row,vertex_column+1
        candidates = filter_candidates(vertex_row, vertex_column,[up, right])
    elif position == (shape[0]-1,shape[1]-1):
        up = vertex_row-1,vertex_column
        left =  vertex_row,vertex_column-1
        candidates = filter_candidates(vertex_row, vertex_column,[up, left])
    elif position[0] == 0:
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        right = vertex_row,vertex_column+1
        candidates = filter_candidates(vertex_row, vertex_column,[down,left, right])
    elif position[0] == shape[0]-1:
        up = vertex_row-1,vertex_column
        left =  vertex_row,vertex_column-1
        right = vertex_row,vertex_column+1
        candidates = filter_candidates(vertex_row, vertex_column,[up, left, right])
    elif position[1] == 0:
        up = vertex_row-1,vertex_column
        down = vertex_row+1,vertex_column
        right = vertex_row,vertex_column+1
        candidates = filter_candidates(vertex_row, vertex_column,[up,down, right])
    elif position[1] == shape[1]-1:
        up = vertex_row-1,vertex_column
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        candidates = filter_candidates(vertex_row, vertex_column,[up, down, left])
    else:
        up = vertex_row-1,vertex_column
        down = vertex_row+1,vertex_column
        left =  vertex_row,vertex_column-1
        right = vertex_row,vertex_column+1
        candidates = filter_candidates(vertex_row, vertex_column,[up, down, left, right])
        
    adjacents = [candidate for candidate in candidates if letter_values[grid[candidate]] <= letter_values[vertex] +1 ]   
    return vertex, adjacents

# not necessary
def adjacency_matrix(grid, nodes) -> pd.DataFrame:
    size = len(nodes)
    shape = size, size
    zero = np.zeros(shape)
    data_frame = pd.DataFrame(data = zero, columns= nodes, index = pd.MultiIndex.from_tuples(nodes))
    for node in nodes:
        vertex_row = node[0]
        vertex_column = node[1]
        _, adjacents = adjacent_vertices(vertex_row, vertex_column, grid)
        for a in adjacents:  
            data_frame[a][node] = 1
            data_frame[node][a] = 1
            
    return data_frame


    







