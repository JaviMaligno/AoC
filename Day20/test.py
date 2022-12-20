from C20 import mixing, multiple_mixing
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day20\test.txt") as f: 
    text = f.read()
    print(multiple_mixing(text, times=10))