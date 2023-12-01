from C15 import no_beacon_1, no_beacon_2, itemgetter
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day15\test.txt") as f: 
    text = f.read()
    print(no_beacon_1(text,row=11,row_limit=20))
    #print(no_beacon_2(text, row=10))