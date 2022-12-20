import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(20)


def composition(dict1, dict2):
    composition_map = {}
    for k in dict1.keys():
        composition_map[k] = dict2[dict1[k]]
    return composition_map

def mixing(numbers, position_dict):
    size = len(numbers)
    for index in range(size):
        number = numbers[position_dict[index]]
        if number == 0:
            continue
            """ elif number < 0:
            current_index = position_dict[index]
            cycles = (number+current_index) // size
            left = numbers[:current_index]
            right = numbers[current_index+1:]
            new_index = (number+current_index+cycles) % size-1 
            if new_index == 6:
                new_index = 0
            diff = new_index - current_index 
            new_dict = dict(zip(range(size), range(size)))
            if diff > 0:
                right_index = diff
                right.insert(right_index, number)
                numbers = left+right
                for i in range(current_index+1,new_index+1):
                    new_dict[i] -=1 
            else:
                left_index = new_index
                left.insert(left_index,number)
                numbers = left+right
                for i in range(new_index,current_index):
                    new_dict[i] +=1"""
        else:
            current_index = position_dict[index]
            cycles = (number+current_index) // size
            left = numbers[:current_index]
            right = numbers[current_index+1:]
            new_index = (number+current_index+cycles) % size or size-1
            diff = new_index - current_index 
            new_dict = dict(zip(range(size), range(size)))
            if diff > 0:
                right_index = diff
                right.insert(right_index, number)
                numbers = left+right
                for i in range(current_index+1,new_index+1):
                    new_dict[i] -=1
            else:
                left_index = new_index
                left.insert(left_index,number)
                numbers = left+right
                for i in range(new_index,current_index):
                    new_dict[i] +=1
            new_dict[current_index] = new_index
            position_dict = composition(position_dict, new_dict)
            
    return numbers, position_dict
    
    

def grove(numbers, zero_index):
    size = len(numbers)
    thousandth = numbers[(zero_index + 1000) % size]
    two_thousandth = numbers[(zero_index + 2000) % size]
    three_thousandth = numbers[(zero_index + 3000) % size]
    grove = thousandth+two_thousandth+three_thousandth
    return grove
#print(mixing(text))

def multiple_mixing(text, KEY = 811589153, times = 10):
    original_numbers = list(map(lambda x: KEY*x, map(int, text.splitlines())))
    zero_index = original_numbers.index(0)
    numbers = original_numbers.copy()
    size = len(numbers)
    position_dict = dict(zip(range(size), range(size)))
    for i in range(times):
        numbers, position_dict = mixing(numbers, position_dict)
    zero_index = position_dict[zero_index]
    final_grove = grove(numbers, zero_index)
    return numbers, final_grove

#811589153 % 7 = 4
# quotient 115941307

#print(multiple_mixing(text, times = 10))