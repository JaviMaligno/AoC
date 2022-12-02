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

    score = sum(draw_values[round] + hand_values[round[1]] for round in rounds)
    return score

#print([(rounds[i][0],rounds[i][2]) for i in range(len(rounds)) ])
print(compute_score(text))