import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input



#By hand because parsing it is a pain in the ass and the input is small enough
stacks = {1: ["G", "J", "W", "R", "F", "T", "Z"], 2:["M", "W", "G"], 3: ["G", "H", "N", "J"],
            4: ["W", "N", "C","R","J"], 5: ["M", "V", "Q", "G", "B", "S", "F", "W"],
            6: ["C", "W", "V", "D","T", "R","S"], 7: ["V", "G", "Z", "D", "C", "N", "B", "H"],
            8: ["C", "G", "M", "N", "J", "S"], 9: ["L", "D", "J", "C", "W", "N", "P", "G"]}
""" 
                [M]     [V]     [L]
[G]             [V] [C] [G]     [D]
[J]             [Q] [W] [Z] [C] [J]
[W]         [W] [G] [V] [D] [G] [C]
[R]     [G] [N] [B] [D] [C] [M] [W]
[F] [M] [H] [C] [S] [T] [N] [N] [N]
[T] [W] [N] [R] [F] [R] [B] [J] [P]
[Z] [G] [J] [J] [W] [S] [H] [S] [G]
 1   2   3   4   5   6   7   8   9 """
text = get_input(5).splitlines()

def get_instructions(text):
    i = 0
    while True:
        if not text[i]:
            break
        else:
            i+=1
    instructions = [tuple(map(int, instruction.split(' ')[1:6:2])) for instruction in text[i+1:]]
    return instructions

def move_crates(a, instruction, stacks, machine = 9000):
    if machine == 9000:
        while a > 0:
            moved = stacks[instruction[1]][0]
            stacks[instruction[2]] = [moved] + stacks[instruction[2]]
            stacks[instruction[1]] = stacks[instruction[1]][1:]
            a -= 1
    elif machine == 9001:
        moved = stacks[instruction[1]][:a]
        stacks[instruction[2]] = moved + stacks[instruction[2]]
        stacks[instruction[1]] = stacks[instruction[1]][a:]

def top_crates(instructions,stacks, machine = 9000):
    for instruction in instructions:
        a = instruction[0]
        move_crates(a,instruction, stacks, machine)
    return ''.join([stacks[i][0] for i in range(1,len(stacks)+1)])

print(top_crates(get_instructions(text), stacks, machine=9001))