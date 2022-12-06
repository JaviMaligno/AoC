from C6 import first_mark

with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day6\test.txt") as f:
    text = f.readlines()
    print([int(line.split(' ')[1]) == first_mark(line, 4) for line in text])
    print([int(line.split(' ')[2][:-1]) == first_mark(line, 14) for line in text[:-1]] + [int(text[-1].split(' ')[2]) == first_mark(text[-1],14)])
    #line4  = text[-2][:-2], text[-2][-2]
    #line5 = text[-1][:-2], text[-1][-2]
    #print(line4, license)

    