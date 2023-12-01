import numpy as np
from math import prod
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(11).splitlines()

def chunk_text(text, n):
    chunks = [[].copy() for i in range(n)]
    chunk_index = 0
    for i in range(len(text)):
        line = text[i]
        if line:
           chunks[chunk_index].append(line)
        else:
            chunk_index+=1
    # chunks = [lines[n:n + 7] for n in range(0, len(lines), 7)] 
    return chunks


def chunk_to_json(chunk)-> dict:
    json = {}
    key = chunk[0].split(' ')[1][:-1] #drop colon
    sub_dict = {}

    items = list(map(int, chunk[1].split(': ')[1].split(', ')))
    sub_dict['items'] = items

    operation = chunk[2].split(': ')[1]
    sub_dict['operation'] = operation

    test = int(chunk[3].split(': ')[1].split(' ')[-1])
    sub_dict['test'] = test

    decision = {}
    true = chunk[4].split(': ')[1].split(' ')[-1]
    false = chunk[5].split(': ')[1].split(' ')[-1]
    decision['true'] = true
    decision['false'] = false

    sub_dict['decision'] = decision

    sub_dict.setdefault('inspect', 0)

    json[key] = sub_dict
    return json

# print(chunk_to_json(chunk_text(text)[7]))

def jsonfy(text, n):  
    chunks = chunk_text(text,n)
    json ={} # ** to merge dictionaries
    for chunk in chunks:
        json.update(chunk_to_json(chunk))
    return json
#print([monkey['operation'] for _,monkey in jsonfy(text).items()])

def modular_operation_parser(operation, value, N,worry_rate = 3):
    binary = operation.split(' ')[-2]
    second = operation.split(' ')[-1]
    number = value if second == 'old' else int(second)
    if binary == '+':
        value += number
    elif binary == '*':
        value *= number

    return (value // worry_rate) %  N

def operation_parser(operation, value,worry_rate = 3):
    binary = operation.split(' ')[-2]
    second = operation.split(' ')[-1]
    number = value if second == 'old' else int(second)
    if binary == '+':
        value += number
    elif binary == '*':
        value *= number

    return (value // worry_rate) 

def rounds(monkeys, n_rounds = 20, modular = True):
    N = prod([monkey['test'] for monkey in monkeys.values()])
    for _ in range(n_rounds): 
        for monkey in monkeys.values():
            items = monkey['items']
            operation = monkey['operation']
            test = monkey['test']
            for item in items:
                monkey['inspect'] += 1
                item = modular_operation_parser(operation, item, N, worry_rate=1) if modular else operation_parser(operation, item, worry_rate=1)
                throw = divisibility_test(item,test,monkey) 
                #item, throw = optimized_throw(index, monkey, operation, test, item, N)
                monkeys[throw]['items'].append(item)
                items = items[1:]
                monkey['items'] = items
    return monkeys


""" def optimized_throw(index, monkey, operation, test, item, N):
     if index in ['0', '1', '5']:        
        throw = divisibility_test(item, test, monkey) 
        item = operation_parser(operation, item) 
    else:
    item = operation_parser(operation, item) 
    throw = divisibility_test(item, test, monkey) 
    return item % N,throw
 """
def divisibility_test(item, test, monkey):
    truth = item % test
    if truth: # the remainder is not 0
        throw = monkey['decision']['false']
    else:
        throw = monkey['decision']['true']
    return throw

monkeys = jsonfy(text, 8)
monkeys = rounds(monkeys, n_rounds = 10000, modular= True)
inspection = [monkey['inspect'] for monkey in monkeys.values()]
largest = max(inspection)
inspection.remove(largest)
second_largest = max(inspection)
level = largest * second_largest
print(level)

def test():
    monkeys = jsonfy(text, 8)
    modular_monkeys = jsonfy(text, 8)
    #print(monkeys.values())
    modular_level = 0
    level = 0
    i = 1
    while level == modular_level and i <= 100:
            modular_monkeys = jsonfy(text, 8)
            modular_monkeys = rounds(modular_monkeys, n_rounds = i, modular= True)
            modular_inspection = [monkey['inspect'] for monkey in modular_monkeys.values()]
            m_largest = max(modular_inspection)
            modular_inspection.remove(m_largest)
            m_second_largest = max(modular_inspection)
            modular_level = m_largest * m_second_largest

            monkeys = jsonfy(text, 8)
            monkeys = rounds(monkeys, n_rounds = i, modular= False)
            inspection = [monkey['inspect'] for monkey in monkeys.values()]
            largest = max(inspection)
            inspection.remove(largest)
            second_largest = max(inspection)
            level = largest * second_largest
            i += 1 
        # print([index for index,monkey in monkeys.items()])
    print(i, level, modular_level)

def test_test():
    monkeys = jsonfy(text, 4)
    modular_monkeys = jsonfy(text, 4)
    #print(monkeys.values())
    modular_level = 0
    level = 0
    i = 1
    with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day11\test.txt") as f: 
        text = f.read().splitlines()
        
        monkeys = jsonfy(text, 4)
        modular_monkeys = jsonfy(text, 4)
        #print(monkeys.values())
        modular_level = 0
        level = 0
        i = 1
        """ modular_monkeys = rounds(modular_monkeys, n_rounds = i, modular= False)
        modular_inspection = [monkey['inspect'] for monkey in modular_monkeys.values()]
        m_largest = max(modular_inspection)
        modular_inspection.remove(m_largest)
        m_second_largest = max(modular_inspection)
        modular_level = m_largest * m_second_largest """
        while level == modular_level and i <= 500:
            modular_monkeys = jsonfy(text, 4)
            modular_monkeys = rounds(modular_monkeys, n_rounds = i, modular= True)
            modular_inspection = [monkey['inspect'] for monkey in modular_monkeys.values()]
            m_largest = max(modular_inspection)
            modular_inspection.remove(m_largest)
            m_second_largest = max(modular_inspection)
            modular_level = m_largest * m_second_largest

            monkeys = jsonfy(text, 4)
            monkeys = rounds(monkeys, n_rounds = i, modular= False)
            inspection = [monkey['inspect'] for monkey in monkeys.values()]
            largest = max(inspection)
            inspection.remove(largest)
            second_largest = max(inspection)
            level = largest * second_largest
            i += 1 
        # print([index for index,monkey in monkeys.items()])
        print(i, level, modular_level)


