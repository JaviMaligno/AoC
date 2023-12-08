from C8 import *
with open(r"AoC2023\Day8\test2.txt") as f: 
    text = f.read()
    dictionary ,instructions = process_input_2(text)
    #print(instructions, dictionary)
    steps = calculate_steps_2(instructions, dictionary)
    print(steps)