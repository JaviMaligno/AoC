import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
import numpy as np
from get_data import get_input
text = list(map(list, get_input(8).splitlines()))


def visible_trees(text):
    matrix = np.array(text).astype(int)
    shape = matrix.shape
    edge = 2*sum(shape)-4
    #print(edge == 97*4 + 4)
    visible = edge

    for  i in range(1,shape[0]-1):
        for j in range(1,shape[1]-1):
            left = np.all(matrix[i,:j] < matrix[i,j])
            right = np.all(matrix[i,j+1:] < matrix[i,j])
            top = np.all(matrix[:i,j] < matrix[i,j])
            bottom = np.all(matrix[i+1:,j] < matrix[i,j])
            visible += any([left,right, top, bottom])
    return visible

#visible = visible_trees(text)
#print(visible)

def best_scenic_score(text):
    matrix = np.array(text).astype(int)
    shape = matrix.shape
    best_score = max(scenic_score(matrix, i, j) for i in range(1,shape[0]-1) for j in range(1,shape[1]-1))
    return best_score

   

def scenic_score(matrix, i,j):
    tree = matrix[i,j]

    left = matrix[i,:j]
    right = matrix[i,j+1:]
    top = matrix[:i,j]
    bottom = matrix[i+1:,j]

    left_score = add_while_short(tree, np.flip(left))
    right_score = add_while_short(tree, right)
    top_score = add_while_short(tree, np.flip(top))
    bottom_score = add_while_short(tree, bottom)

    score = left_score * right_score * top_score * bottom_score
    return score

def add_while_short(tree, view):
    score = 0
    for height in view:
        if height < tree:
            score += 1
        else:
            score +=1
            break
    return score

#print(best_scenic_score(text))
    




