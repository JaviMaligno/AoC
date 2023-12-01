import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input

text = get_input(6)

def first_mark(text, chars):
    for i in range(len(text)-chars):
        chunk = set(text[i:i+chars])
        if len(chunk) == chars:
            return i+chars
    else:
        return "No mark"

print(first_mark(text,4), first_mark(text, 14))

