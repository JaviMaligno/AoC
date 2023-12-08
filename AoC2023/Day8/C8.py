import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(8)

def process_input(input_string):
    lines = input_string.split('\n')
    instructions = lines[0]
    dictionary = {}
    for line in lines[1:]:
        if line:
            key, value = line.split(' = ')
            dictionary[key] = tuple(value.strip('()').split(', '))
    return dictionary, instructions, 

def count_steps(instructions, dictionary, start='AAA', target='ZZZ'):
    steps = 0
    current = start
    while current != target:
        for instruction in instructions:
            if instruction == 'L':
                current = dictionary[current][0]
            else:
                current = dictionary[current][1]
            steps += 1
            if current == target:
                break
    return steps



#instructions, dictionary = process_input(text)
#steps = count_steps(instructions, dictionary)
#print(f"It takes {steps} steps to reach 'ZZZ'.")

def process_input_2(input_string):
    lines = input_string.split('\n')
    instructions = lines[0]
    dictionary = {}
    for line in lines[1:]:
        if line:
            key, value = line.split(' = ')
            dictionary[key] = tuple(value.strip('()').split(', '))
    return instructions, dictionary


from collections import deque

def calculate_steps_2(nodes, instructions):
    # Function to calculate steps
    def bfs(start_node, end_node):
        queue = deque([(start_node, 0)])
        visited = set()

        while queue:
            node, steps = queue.popleft()
            if node == end_node:
                return steps

            next_node = nodes[node][0] if instructions[steps % len(instructions)] == 'L' else nodes[node][1]
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, steps + 1))

    # Initialize the results dictionary
    results = {}

    # Calculate steps for each starting node
    for node in nodes:
        if node[-1] == 'A':
            steps_to_end = bfs(node, node[:-1] + 'Z')
            extra_steps = bfs(node[:-1] + 'Z', node[:-1] + 'Z')
            results[node] = (steps_to_end, extra_steps)

    return results


graph = {
    '11A': ['11B', 'XXX'],
    '11B': ['XXX', '11Z'],
    '11Z': ['11B', 'XXX'],
    '22A': ['22B', 'XXX'],
    '22B': ['22C', '22C'],
    '22C': ['22Z', '22Z'],
    '22Z': ['22B', '22B'],
    'XXX': ['XXX', 'XXX']
}

instructions = "LR"

def traverse_graph(graph, instructions):
    # Find starting nodes
    start_nodes = [node for node in graph.keys() if node.endswith('A')]
    results = []

    for start in start_nodes:
        node = start
        path = [node]
        instruction_index = 0

        # Follow instructions
        while True:
            instruction = instructions[instruction_index % len(instructions)]
            if instruction == 'L':
                node = graph[node][0]
            elif instruction == 'R':
                node = graph[node][1]
            path.append(node)
            instruction_index += 1

            # Stop if we've reached an ending node twice
            if node.endswith('Z') and path.count(node) == 2:
                break

        # Find the number of steps to reach the ending node and to come back to it
        first_Z_index = path.index(next(x for x in path if x.endswith('Z')))
        steps_to_Z = first_Z_index
        steps_to_same_Z = len(path) - first_Z_index - 1

        results.append((start, steps_to_Z, steps_to_same_Z))

    return results


print(traverse_graph(graph, instructions))

from sympy import symbols, Eq, solve

def find_common_number(tuples):
    # Create a symbol for the common number
    x = symbols('x')

    # Create the list of equations
    equations = [Eq((x - a) % b, 0) for a, b in tuples]

    # Solve the system of equations
    solutions = solve(equations)

    # Return the smallest positive solution
    return min(sol.evalf() for sol in solutions if sol.is_positive)






#print(find_smallest_common_number(tuples))







instructions, nodes = process_input_2(text)

steps = traverse_graph(nodes, instructions)
#print(steps)
tuples = [(a,b) for (_,a,b) in steps]
print(tuples)


from math import gcd
a = [b for a,b in tuples]   #will work for an int array of any length
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)

# rint(find_common_number(tuples))
#steps = count_steps(instructions, dictionary)
#print(f"It takes {steps} steps for all starting nodes to reach an ending node.")
