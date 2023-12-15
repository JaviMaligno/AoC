from C15 import *
with open(r"Day15\test.txt") as f: 
    text = f.read()
    strings = text.split(",")
    print(hash_algorithm(strings))