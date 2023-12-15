import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(15)

strings = list(map(lambda x: x.strip(),text.split(",")))
def hash_string(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def hash_algorithm(strings):
    total = 0
    for string in strings:
        total += hash_string(string)
    return total 

print(hash_algorithm(strings))

# Part 2 doesn'r explain how the boxes are chosen so I'm not doing it