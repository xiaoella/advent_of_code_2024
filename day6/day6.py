"""
Day 6 Part 1
"""
# input file
with open("day6/input.txt", "r") as file:
    map = file.read().split("\n")

# function to move guard in map
def move_guard(x, y, direction):
    if direction == "start" and map[x-1] != "#":
            return (x-1, y, "up")
    elif direction == "up":
        if x-1 >= 0 and map[x-1][y] != "#":
            return (x-1, y, "up")
        elif map[x-1][y] == "#" and y+1 < len(map[x]):
            return (x, y+1, "right")
    elif direction == "right":
        if y+1 < len(map[x]) and map[x][y+1] != "#":
            return (x, y+1, "right")
        elif map[x][y+1] == "#" and x+1 < len(map):
            return (x+1, y, "down")
    elif direction == "down":
        if x+1 < len(map) and map[x+1][y] != "#":
            return (x+1, y, "down")
        elif y-1 >= 0 and map[x+1][y] == "#":
            return (x, y-1, "left")
    elif direction == "left":
        if y-1 >= 0 and map[x][y-1] != "#":
            return (x, y-1, "left")
        elif x-1 >= 0 and map[x][y-1] == "#":
            return (x-1, y, "up")
    return (x, y, "stop")
    
def main():
    # Find initial guard position
    guardx, guardy = 0, 0
    for x, row in enumerate(map):
        for y, char in enumerate(row):
            if char == "^":
                guardx, guardy = x, y
                break

    # Initialise variables
    direction = "start"
    positions = [(guardx, guardy)]

    # Guard movement loop
    while True:
        guardx, guardy, direction = move_guard(guardx, guardy, direction)
        positions.append((guardx, guardy))
        if direction == "stop":
            break

    print(f"Distinct positions of guard: {len(set(positions))}")

if __name__ == "__main__":
    main()