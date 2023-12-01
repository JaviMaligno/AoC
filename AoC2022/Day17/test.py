from C17 import ROCKS, BOARD, tetris
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day17\test.txt") as f: 
    text = f.read()
    #print(text)
    print(tetris(text, BOARD, ROCKS,2022)[0])
    