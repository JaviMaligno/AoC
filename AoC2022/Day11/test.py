from C11 import jsonfy, rounds, operation_parser
from math import  prod
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day11\test.txt") as f: 
    text = f.read().splitlines()
    
    monkeys = jsonfy(text,4)
    # print(monkeys)
    monkeys = rounds(monkeys, n_rounds=1000, modular=True)
    inspection = [monkey['inspect'] for monkey in monkeys.values()]
    largest = max(inspection)
    inspection.remove(largest)  
    second_largest = max(inspection)
    level = largest * second_largest
    print(largest, second_largest)

    