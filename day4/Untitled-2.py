"""
Day 5 Part 1
"""

with open("day5/rule.txt", "r") as file:
    rule = file.read().split("\n")

with open("day5/input.txt", "r") as file:
    data = file.read().split("\n")

# cleaning the rule pairs into a list
rule = [pair.split("|") for pair in rule]

# cleaning the data
data = [row.split(",") for row in data]

# function to check if a row passes the rule
def check_row(row) -> bool:
    for i, num in enumerate(row):
        if i == 0:
            continue
        for pair in rule:
            if num == pair[0]:
                for j in range(i):
                    if row[j] == pair[1]:
                        return False
    return True


# initialising counter for adding in the middle number
counter = 0

for row in data:
    if check_row(row):
        counter += int(row[len(row)//2])

print(f"Sum of middle page numbers in correctly ordered data: {counter}")