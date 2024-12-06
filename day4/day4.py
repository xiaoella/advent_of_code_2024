"""
Day 4 Part 1
"""


# import input
with open("day4/input.txt", "r") as file:
    data = file.read()

# splitting into rows
data = data.split("\n")

directions = [
    (-1, 0),    # North
    (-1, 1),    # North-east
    (0, 1),     # East
    (1, 1),     # South-east
    (1, 0),     # South
    (1, -1),    # South-west
    (0, -1),    # West
    (-1, -1)    # North-west
]

# function to move scanning tile along i,j direction
def move_tile(data, x, y, i, j, step) -> str:
    new_x = x + i * step
    new_y = y + j * step
    # ensuring scanning tile is within the edges of data
    if 0 <= new_x < len(data) and 0 <= new_y < len(data[x]):
        return data[new_x][new_y]
    return None

# function to scan 'XMAS' within data in sequence
def scanner(data: list[str], x: int, y: int, i: int, j: int) -> bool:
    if data[x][y] == "X":
            if move_tile(data, x, y, i, j, 1) == "M":
                if move_tile(data, x, y, i, j, 2) == "A":
                    if move_tile(data, x, y, i, j, 3) == "S":
                        return True
    return False

counter = 0
for x, row in enumerate(data):
    for y, char in enumerate(row):
        for direction in directions:
            i, j = direction
            if scanner(data, x, y, i, j):
                counter += 1

print(f"Number of 'XMAS' in data: {counter}")


"""
Part 2
"""
def scan_x(data, x, y) -> bool:
    if x <= 0 or x >= len(data)-1 or y <= 0 or y >= len(data[0])-1:
        return False
    # first X \
    top_left = data[x-1][y-1]
    bot_right = data[x+1][y+1]
    # second X /
    bot_left = data[x-1][y+1]
    top_right = data[x+1][y-1]
    # checking if both \/ makes up MAS in any combination
    if ((top_left, bot_right) in [("M", "S"), ("S", "M")]) and ((bot_left, top_right) in [("M", "S"), ("S", "M")]):
        return True

counter = 0
for x, row in enumerate(data):
    for y, char in enumerate(row):
        if data[x][y] == "A":
            if scan_x(data, x, y):
                counter += 1

print(f"Number of 'X-MAS' in data: {counter}")