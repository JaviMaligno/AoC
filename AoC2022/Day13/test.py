from C13 import chunked, packeted, compare, sort
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day13\test.txt") as f: 
    text = f.read()
    #chunks = chunked(text)
    #ordered = compare(chunks)
    #print(ordered)
    packets= packeted(text)
    print(packets)
    sorted_packets = sort(packets)
    print(sorted_packets)