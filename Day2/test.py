from C2 import compute_score

with open(r'C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day2\test1.txt') as text:
    text = text.read()
    score = compute_score(text)
    print(score == 15)

