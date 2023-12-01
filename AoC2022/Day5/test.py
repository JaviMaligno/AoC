""" import numpy  as np
Tried to parse it with numpy but it also requires preprocessing, I'm not doing this for free

numpy_text = np.loadtxt(r"Day5\test.txt", delimiter=' ', dtype=str)
print(numpy_text) 

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
from C5 import get_instructions, top_crates

stacks = {1: ["N", "Z"], 2: ["D", "C", "M"], 3: ["P"]}

with open(r"Day5\test.txt") as f:
    text = f.read().splitlines()
    instructions = get_instructions(text)
    print(top_crates(instructions, stacks) == "CMZ")
    print(top_crates(instructions, stacks, machine=9001))