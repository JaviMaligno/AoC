import ast
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(13)

def packeted(text):
    lines = text.splitlines()
    packets = list(ast.literal_eval(line) for line in lines if line)
    return packets

def chunked(text):
    lines = text.splitlines()
    chunks = [ list(map(ast.literal_eval,lines[n:n+3][:2])) for n in range(0, len(lines), 3)]
    return chunks

class comp_list(list):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    def __le__(self, x) -> bool:
        if isinstance(x, int):
            return super().__le__([x])
        else:
            return super().__le__(x)
        
    def __lt__(self, x) -> bool:
        if isinstance(x, int):
            return super().__lt__([x])
        else:
            return super().__lt__(x)

class comp_int(int):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    def __le__(self,x) -> bool:
        if isinstance(x, list):
            return list([self]).__le__(x)
        else:
            return super().__le__(x)

    def __lt__(self,x) -> bool:
        if isinstance(x, list):
            return list([self]).__lt__(x)
        else:
            return super().__lt__(x)

def comp(item):
    if isinstance(item, int):
        return comp_int(item)
    else:
        return comp_list([comp(x) for x in item])

# print(comp_int(3), comp_list([1,2]), comp_int(3) <= comp_list([1,2]), comp_list([1,2]) <= comp_int(3))



def compare(chunks):
    ordered = 0
    for i, chunk in enumerate(chunks):
            left_value = comp(chunk[0])
            right_value = comp(chunk[1])
            ordered = ordered + i+1 if left_value <= right_value else ordered
    return ordered
chunks = chunked(text)
packets = packeted(text)

def sort(packets):
    divider1 = [[2]]
    divider2 = [[6]]
    packets = packets + [divider1,divider2]
    packets = comp(packets)
    sort_packets = sorted(packets)
    index1 = sort_packets.index(divider1)+1
    index2 = sort_packets.index(divider2)+1
    return index1*index2

divider1 = [[2]]
divider2 = [[6]]

# this one gives the correct answer, why is it different?
def sort_two(packets, divider1, divider2):
    packets = comp(packets)
    divider1 = comp(divider1)
    divider2 = comp(divider2)
    index1 = sum([1 for packet in packets if packet < divider1 ])+1
    index2 = 1+sum([1 for packet in packets if packet < divider2 ])+1
    return index1*index2, index1, index2

def sort_two_relaxed(packets, divider1, divider2):
    packets = comp(packets)
    divider1 = comp(divider1)
    divider2 = comp(divider2)
    index1 = sum([1 for packet in packets if packet <= divider1 ])+1
    index2 = 1+sum([1 for packet in packets if packet <= divider2 ])+1
    return index1*index2, index1, index2
print(sort(packets), sort_two(packets, divider1, divider2), sort_two_relaxed(packets, divider1, divider2))

equal1 = [packet for packet in packets if comp(packet) <= comp(divider1) and not(comp(packet) < comp(divider1))]
print(equal1[0] <= [[[2]]]) 
print(comp(equal1[0]) <= comp(divider1)) #this is giving True  but shouldn't I don't know why
print(equal1)


    





    
