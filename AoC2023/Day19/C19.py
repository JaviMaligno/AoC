import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(19)

def parse_string(s):
    # Remove the braces at the beginning and end of the string
    s = s[1:-1]
    
    # Split the string into pairs of 'variable=value'
    pairs = s.split(',')
    
    # Initialize an empty dictionary to store the variable-value pairs
    variables = {}
    
    for pair in pairs:
        # Split the pair into variable and value
        variable, value = pair.split('=')
        
        # Assign the value to the variable in the dictionary
        variables[variable] = int(value)
    
    return variables

# Test the function with your example string
""" s = "{x=787,m=2655,a=1222,s=2876}"
variables = parse_string(s) """

#print(variables)  # Output: {'x': 787, 'm': 2655, 'a': 1222, 's': 2876}

def parse_input(input_string):
    # Split the input string into instructions and variable dictionaries
    instructions_string, variable_dicts_string = input_string.split('\n\n')
    
    # Split the instructions string into a list of instructions
    instructions = instructions_string.split('\n')
    
    # Split the variable dictionaries string into a list of variable dictionary strings
    variable_dict_strings = variable_dicts_string.split('\n')
    
    # Parse each variable dictionary string into a dictionary
    variable_dicts = [parse_string(s) for s in variable_dict_strings]
    
    return instructions, variable_dicts

# Test the function with your example input
input_string = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".strip()

input_string = text.strip()
instructions, variable_dicts = parse_input(input_string)

#print("Instructions:", instructions)  # Output: Instructions: ['px{a<2006:qkq,m>2090:A,rfg}', 'pv{a>1716:R,A}', 'lnx{m>1548:A,A}', 'rfg{s<537:gd,x>2440:R,A}', 'qs{s>3448:A,lnx}', 'qkq{x<1416:A,crn}', 'crn{x>2662:A,R}', 'in{s<1351:px,qqz}', 'qqz{s>2770:qs,m<1801:hdj,R}', 'gd{a>3333:R,R}', 'hdj{m>838:A,pv}']
#print("Variable dictionaries:", variable_dicts)  # Output: Variable dictionaries: [{'x': 787, 'm': 2655, 'a': 1222, 's': 2876}, {'x': 1679, 'm': 44, 'a': 2067, 's': 496}, {'x': 2036, 'm': 264, 'a': 79, 's': 2244}, {'x': 2461, 'm': 1339, 'a': 466, 's': 291}, {'x': 2127, 'm': 1623, 'a': 2188, 's': 1013}]

def execute_instructions(instructions, variables, initial_instruction):
    # Find the initial instruction
    for instruction in instructions:
        if instruction.startswith(initial_instruction):
            # Split the instruction into its name and conditions
            name, conditions = instruction.split('{')
            conditions = conditions[:-1].split(',')
            
            # Loop through the conditions
            for i, condition in enumerate(conditions):
                # Check if this is the last condition
                if i == len(conditions) - 1:
                    action = condition
                    # If the action is an instruction name, find and execute that instruction
                    if action not in ['A', 'R']:
                        return execute_instructions(instructions, variables, action)
                else:
                    # Split the condition into its parts
                    variable, rest = condition.split('<' if '<' in condition else '>')
                    comparison, action = rest.split(':')
                    
                    # Check if the condition holds
                    if ('<' in condition and variables[variable] < int(comparison)) or \
                       ('>' in condition and variables[variable] > int(comparison)):
                        # If the action is 'A' or 'R', return it
                        if action in ['A', 'R']:
                            return action
                        
                        # Otherwise, find the instruction with the given name and execute it
                        else:
                            return execute_instructions(instructions, variables, action)
    
    # If none of the conditions hold, return the last action
    return action

    
    # If none of the conditions hold, execute the last action
    return action
""" instructions = ["px{a<2006:qkq,m>2090:A,rfg}"]
variables = {'x': 787, 'm': 2655, 'a': 1222, 's': 2876}
result = execute_instructions(instructions, variables) """

#print(result)  # Output: 'A'

def process_variables_and_instructions(variable_dicts, instructions):
    # Initialize a list to store the accepted dictionaries
    accepted_dicts = []
    
    # Loop through the variable dictionaries
    for variables in variable_dicts:
        # Execute the instructions for each dictionary
        result = execute_instructions(instructions, variables, 'in')


        # If the result is 'A', add the dictionary to the accepted list
        if result == 'A':
            accepted_dicts.append(variables)
    
    # Sum the values of all the variables in the accepted dictionaries
    total_sum = sum(sum(variables.values()) for variables in accepted_dicts)
    
    return total_sum, accepted_dicts

# Test the function with your example instructions and variable dictionaries
# instructions = ["in{a<2006:qkq,m>2090:A,rfg}"]
# variable_dicts = [{'x': 787, 'm': 2655, 'a': 1222, 's': 2876}, {'x': 500, 'm': 1500, 'a': 1000, 's': 2000}]
total_sum, accepted_dicts = process_variables_and_instructions(variable_dicts, instructions)
#print(instructions)
print("Total sum:", total_sum)  # Output: Total sum: 7640
#print("Accepted dictionaries:", accepted_dicts)  # Output: Accepted dictionaries: [{'x': 787, 'm': 2655, 'a': 1222, 's': 2876}]
