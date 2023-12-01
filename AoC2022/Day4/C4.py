import sys
from string import ascii_lowercase, ascii_uppercase
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input

text = get_input(4)

def overlap(text):
    pairs = list(map(lambda pair: tuple(map(lambda x: set(range(int(x.split("-")[0]), int(x.split("-")[1])+1)), pair.split(","))), text.splitlines()))
    included = sum(x.issubset(y) or y.issubset(x) for x,y in pairs)
    intersect = sum( bool(x.intersection(y)) for x,y in pairs)
    return included, intersect


    