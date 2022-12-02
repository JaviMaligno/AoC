from C2 import compute_score, second_round

with open(r'test1.txt') as text:
    text = text.read()
    score = compute_score(text)
    score2 = second_round(text)
    print(score == 15)
    print(score2 == 12)

#C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day2