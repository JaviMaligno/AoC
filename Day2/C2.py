from decouple import config
import requests
from itertools import product, cycle


AOC_SESSION = config('AOC_SESSION')


s = requests.Session()
s.auth = ('JaviMaligno', '76321jav')
resp = s.get('https://adventofcode.com/2022/day/2/input', cookies={'session':AOC_SESSION})
text = resp.text
def compute_score(text):
    rounds = list(map(lambda x: (x[0], x[2]), text.splitlines()))
    my_encrypt = ['X','Y','Z']
    hand_points = [1,2,3]
    hand_values = dict(zip(my_encrypt, hand_points))
    op_encrypt = ['A','B','C'] 
    draws = list(product(op_encrypt,my_encrypt))
    draw_points = [3,6,0, 0,3,6, 6,0,3]
    draw_values = dict(zip(draws,draw_points))
    score2 = 0
    score = sum(draw_values[round] + hand_values[round[1]] for round in rounds)
    return score

#print([(rounds[i][0],rounds[i][2]) for i in range(len(rounds)) ])
def second_round(text):
    rounds = list(map(lambda x: (x[0], x[2]), text.splitlines()))
    my_encrypt = ['X','Y','Z']
    op_encrypt = ['A','B','C'] 
    hand_points = [1,2,3]
    hand_values = dict(zip(op_encrypt, hand_points))
    win = {'A':'B', 'B':'C', 'C':'A'}
    draw = dict(zip(op_encrypt,op_encrypt)) 
    lose = {'A' : 'C', 'B':'A', 'C':'B'}
    points = zip(my_encrypt,[0,3,6])
    # draws = list(product(op_encrypt,my_encrypt))
    score = 0
    for round in rounds:
        result = round[1]
        result_points = points(result)
        opponent = round[0]
        if result == 'X':
            result_points += hand_values[lose[opponent]]
        elif result == 'Y':
            result_points += hand_values[draw[opponent]]
        else:
            result_points += hand_values[win[opponent]]
        score += result_points
    return score