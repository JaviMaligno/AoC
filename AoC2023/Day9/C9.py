import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
from get_data import get_input
text = get_input(9)

def convert_text_to_lists(text):
    # Split the text into lines
    lines = text.splitlines()
    
    # For each line, split it into numbers and convert each number to an integer
    lists = [[int(num) for num in line.split()] for line in lines]
    
    return lists

def compute_differences(lst):
    # Initialize the list of differences
    differences = []
    
    # While the list is not all zeros
    while any(lst):
        # Compute the differences between consecutive elements
        lst = [j-i for i, j in zip(lst[:-1], lst[1:])]
        
        # Add the list of differences to the result
        differences.append(lst)
    
    return differences

def extrapolate_next_element(lst):
    # Compute the lists of differences
    differences = compute_differences(lst)
    
    # Add a zero to the last list of differences
    differences[-1].append(0)
    
    # Reverse the process
    for i in range(len(differences) - 2, -1, -1):
        # Add an element to the list such that the difference with the last element is 0
        differences[i].append(differences[i][-1] + differences[i+1][-1])
    
    # Add the extrapolated element to the original list
    lst.append(lst[-1] + differences[0][-1])
    
    return lst

#lst = [10, 13, 16, 21, 30, 45]
#print(extrapolate_next_element(lst))

def extrapolate_and_sum(lists):
    # Initialize the sum
    total = 0
    
    # For each list
    for lst in lists:
        # Compute the extrapolated value
        extrapolated_list = extrapolate_next_element(lst)
        
        # Add the extrapolated value to the sum
        total += extrapolated_list[-1]
    
    return total
#lists = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
lists = convert_text_to_lists(text)
#print(extrapolate_and_sum(lists))

def extrapolate_first_element(lst):
    # Compute the lists of differences
    differences = compute_differences(lst)
    
    # Add a zero to the beginning of the last list of differences
    differences[-1].insert(0, 0)
    
    # Reverse the process
    for i in range(len(differences) - 2, -1, -1):
        # Add an element to the beginning of the list such that the difference with the first element is 0
        differences[i].insert(0, differences[i][0] - differences[i+1][0])
    
    # Add the extrapolated element to the beginning of the original list
    lst.insert(0, lst[0] - differences[0][0])
    
    return lst

#lst = [10,  13,  16,  21,  30,  45]
#print(extrapolate_first_element(lst))

def extrapolate_first_and_sum(lists):
    # Initialize the sum
    total = 0
    
    # For each list
    for lst in lists:
        # Compute the extrapolated value
        extrapolated_list = extrapolate_first_element(lst)
        
        # Add the extrapolated value to the sum
        total += extrapolated_list[0]
    
    return total

#lists = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
print(extrapolate_first_and_sum(lists))
