from C13 import *
with open(r"Day13\test.txt") as f: 
    text = f.read()
    print(process_and_score_patterns(text))
    print(process_and_score_almost_patterns(text))