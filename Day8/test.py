from C8 import visible_trees, best_scenic_score

with open(r"Day8\test.txt") as f:
    text = list(map(list,f.read().splitlines()))
    print(visible_trees(text) == 21)
    print(best_scenic_score(text) == 8)
