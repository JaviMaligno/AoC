import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(17)

def process_grid(grid_string):
    return [[int(num) for num in line] for line in grid_string.strip().splitlines()]



grid_string = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

grid = process_grid(grid_string)


def min_path_sum(grid):
    n, m = len(grid), len(grid[0])
    dp = [[[[float('inf')] * 4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    # Initialize the dp table
    for d in range(4):
        dp[0][0][d][1] = grid[0][0]

    for i in range(n):
        for j in range(m):
            for d in range(4):  # check all directions
                for step in range(1, 4):  # can't go in the same direction more than 3 steps
                    ni, nj = i - directions[d][0], j - directions[d][1]
                    if 0 <= ni < n and 0 <= nj < m:
                        for prev_d in range(4):  # check all previous directions
                            if prev_d == d:  # same direction
                                if step < 3:
                                    dp[i][j][d][step] = min(dp[i][j][d][step], dp[ni][nj][prev_d][step-1] + grid[i][j])
                            else:  # different direction
                                dp[i][j][d][1] = min(dp[i][j][d][1], dp[ni][nj][prev_d][step] + grid[i][j])

    return min(min(dp[-1][-1]))




#print(min_path_sum(grid))
import sys

# Directions: up, right, down, left
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def min_path(grid):
    n, m = len(grid), len(grid[0])
    dp = [[[sys.maxsize]*4 for _ in range(m)] for _ in range(n)]
    dp[0][0] = [grid[0][0]]*4

    for i in range(n):
        for j in range(m):
            for d in range(4):
                for k in range(1, 4):
                    nx, ny = i + dx[d]*k, j + dy[d]*k
                    if is_valid(nx, ny, n, m):
                        dp[i][j][d] = min(dp[i][j][d], dp[nx][ny][(d+2)%4] + grid[i][j])

    return min(dp[n-1][m-1])

# Test the function
grid = [
    [2,4,1,3,4,3,2,3,1,1,3,2,3],
    [3,2,1,5,4,5,3,5,3,5,6,2,3],
    [3,2,5,5,2,4,5,6,5,4,2,5,4],
    [3,4,4,6,5,8,5,8,4,5,4,5,2],
    [4,5,4,6,6,5,7,8,6,7,5,3,6],
    [1,4,3,8,5,9,8,7,9,8,4,5,4],
    [4,4,5,7,8,7,6,9,8,7,7,6,6],
    [3,6,3,7,8,7,7,9,7,9,6,5,3],
    [4,6,5,4,9,6,7,9,8,6,8,8,7],
    [4,5,6,4,6,7,9,9,8,6,4,5,3],
    [1,2,2,4,6,8,6,8,6,5,5,6,3],
    [2,5,4,6,5,4,8,8,8,7,7,3,5],
    [4,3,2,2,6,7,4,6,5,5,5,3,3]
]

print(min_path(grid))




