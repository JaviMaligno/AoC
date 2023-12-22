import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(21)



def reachable_tiles(grid, x, y, max_steps):
    reachable = [set() for _ in range(max_steps + 1)]
    reachable[0].add((x, y))
    for steps in range(max_steps):
        for x, y in reachable[steps]:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] != '#':
                    reachable[steps + 1].add((nx, ny))
    return len(reachable[max_steps])

grid = [
    list("..........."),
    list(".....###.#."),
    list(".###.##..#."),
    list("..#.#...#.."),
    list("....#.#...."),
    list(".##..S####."),
    list(".##..#...#."),
    list(".......##.."),
    list(".##.#.####."),
    list(".##..##.##."),
    list("...........")
]

grid = text.splitlines()
start = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S'][0]
print(reachable_tiles(grid, start[0], start[1], 64))


def reachable_tiles(grid, x, y, max_steps):
    reachable = [set() for _ in range(max_steps + 1)]
    reachable[0].add((x, y, 0, 0))  # Include offsets in state
    for steps in range(max_steps):
        for x, y, dx, dy in reachable[steps]:
            for ddx, ddy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = (x + ddx) % len(grid), (y + ddy) % len(grid[0])
                ndx, ndy = dx + (ddx if nx == 0 else 0), dy + (ddy if ny == 0 else 0)  # Update offsets
                if grid[nx][ny] != '#':
                    reachable[steps + 1].add((nx, ny, ndx, ndy))
    return len(reachable[max_steps])

grid = [
    list("..........."),
    list(".....###.#."),
    list(".###.##..#."),
    list("..#.#...#.."),
    list("....#.#...."),
    list(".##..S####."),
    list(".##..#...#."),
    list(".......##.."),
    list(".##.#.####."),
    list(".##..##.##."),
    list("...........")
]

start = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S'][0]
print(reachable_tiles(grid, start[0], start[1], 10))
