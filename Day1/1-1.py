import numpy as np

def int_or_empty(l):
    for i in range(len(l)):
        l[i] = int(l[i]) if l[i] else 0
    return sum(l)

with open('input1.txt') as f:
    lines = f.readlines()
    list_strings = ''.join(lines).replace('\n\n', ' ').split(' ')
    #print(list_strings)
    string_numbers = list(map(lambda x: x.split('\n'), list_strings))
    sums = list(map(int_or_empty, string_numbers))
    max_sum = max(map(int_or_empty, string_numbers))
    array_sums = np.array(sums)
    temp = np.partition(-array_sums, 3)
    result = -temp[:3]
    print(result.sum())
    print(max_sum)





        


