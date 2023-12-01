import sys
from string import ascii_lowercase, ascii_uppercase
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input

text = get_input(3)
priorities = dict(zip(ascii_lowercase+ascii_uppercase, range(1,53)))



# all(len(x) % 2 == 0 for x in text.splitlines())) # all rucksacks can be divided into 2 equal compartimennts
def compute_priority(text):
    priority = 0
    rucksacks = text.splitlines()
    for rucksack in rucksacks:
        size = len(rucksack)//2
        first = set(rucksack[:size]) # I only care if there is a repeated character, not how many times
        second = set(rucksack[size:])
        repeated = first.intersection(second)
        rucksack_priority = sum(priorities[item] for item in repeated)
        priority += rucksack_priority
    
    return(priority)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# print(all(len(set.intersection(*list(map(lambda x:set(x),group)))) == 1 for group in groups))
# all intersections are singletons

def compute_group_priority(text):
    rucksacks = text.splitlines()
    groups = list(chunks(rucksacks,3))
    priority = 0
    for group in groups:
        group_sets = tuple(map(set,group))
        badge = tuple(set.intersection(*group_sets))[0]
        priority += priorities[badge]
    
    return priority

