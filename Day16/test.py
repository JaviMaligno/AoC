from C16 import graph, recursive_flow, letter_to_number
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day16\test.txt") as f: 
    text = f.read()
    valves = graph(text)
    #print(valves)
    #numerical_valves =letter_to_number(valves)
    #print(len(numerical_valves))
    flow = recursive_flow(valves, time= 30)
    print(flow)