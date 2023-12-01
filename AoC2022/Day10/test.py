from C10 import get_commands, strength, pixels, picture, check_points, X, rows
with open(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022\Day10\test.txt") as f:
    text = f.read()
    commands = get_commands(text)
    s = strength(commands, X, check_points)
    print(s == 13140)
    rows = pixels(commands, rows)
    picture(rows)