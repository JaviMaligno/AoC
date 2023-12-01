from C4 import overlap

with open(r"Day4\test.txt") as f:
    text = f.read()
    print(overlap(text)==(2,4))