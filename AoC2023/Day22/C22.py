import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(22)

bricks = [
    ((1,0,1),(1,2,1)),
    ((0,0,2),(2,0,2)),
    ((0,2,3),(2,2,3)),
    ((0,0,4),(0,2,4)),
    ((2,0,5),(2,2,5)),
    ((0,1,6),(2,1,6)),
    ((1,1,8),(1,1,9))
]

# Sort the bricks by their highest z-coordinate
bricks.sort(key=lambda b: max(b[0][2], b[1][2]))

# Initialize the z-coordinates of the ground and the top of each brick
ground = [1] * len(bricks)
top = [max(b[0][2], b[1][2]) for b in bricks]

# Simulate the falling of each brick
for i in range(len(bricks)):
    for j in range(i):
        if (bricks[i][0][0] <= bricks[j][1][0] and bricks[i][1][0] >= bricks[j][0][0] and
            bricks[i][0][1] <= bricks[j][1][1] and bricks[i][1][1] >= bricks[j][0][1]):
            ground[i] = max(ground[i], top[j] + 1)
    top[i] = max(top[i], ground[i] + min(bricks[i][0][2], bricks[i][1][2]) - 1)

# Determine which bricks are removable
removable = [True] * len(bricks)
for i in range(len(bricks) - 1, -1, -1):
    for j in range(i + 1, len(bricks)):
        if (removable[j] and
            bricks[i][0][0] <= bricks[j][1][0] and bricks[i][1][0] >= bricks[j][0][0] and
            bricks[i][0][1] <= bricks[j][1][1] and bricks[i][1][1] >= bricks[j][0][1] and
            top[i] == ground[j] - 1):
            removable[i] = False
            break

# Count the number of removable bricks
num_removable = sum(removable)
print("Number of removable bricks:", num_removable)



bricks = [
    ((1,0,1),(1,2,1)),
    ((0,0,2),(2,0,2)),
    ((0,2,3),(2,2,3)),
    ((0,0,4),(0,2,4)),
    ((2,0,5),(2,2,5)),
    ((0,1,6),(2,1,6)),
    ((1,1,8),(1,1,9))
]

# Sort the bricks by their lowest z-coordinate
bricks.sort(key=lambda b: min(b[0][2], b[1][2]))

# Initialize the z-coordinates of the ground and the top of each brick
ground = [1] * len(bricks)
top = [max(b[0][2], b[1][2]) for b in bricks]

# Simulate the falling of each brick
for i in range(len(bricks)):
    for z in range(min(bricks[i][0][2], bricks[i][1][2]), max(bricks[i][0][2], bricks[i][1][2]) + 1):
        for j in range(i):
            if (bricks[i][0][0] <= bricks[j][1][0] and bricks[i][1][0] >= bricks[j][0][0] and
                bricks[i][0][1] <= bricks[j][1][1] and bricks[i][1][1] >= bricks[j][0][1] and
                z == top[j] + 1):
                ground[i] = max(ground[i], z)
                break
        if ground[i] > z:
            break
    top[i] = max(top[i], ground[i] + min(bricks[i][0][2], bricks[i][1][2]) - 1)

# Determine which bricks are removable
removable = [True] * len(bricks)
for i in range(len(bricks) - 1, -1, -1):
    for j in range(i + 1, len(bricks)):
        if (removable[j] and
            bricks[i][0][0] <= bricks[j][1][0] and bricks[i][1][0] >= bricks[j][0][0] and
            bricks[i][0][1] <= bricks[j][1][1] and bricks[i][1][1] >= bricks[j][0][1] and
            top[i] == ground[j] - 1):
            removable[i] = False
            break

# Count the number of removable bricks
num_removable = sum(removable)
print("Number of removable bricks:", num_removable)
