"""
Part 1

Note: I am aware that using regular expression
will be the NORMAL way approaching this task...
But I thought I'll give it a go without using re! :)
"""

# import input
with open("day3/input.txt", "r") as file:
    data = file.read()

# function to filter out valid multiplication pairs
def validation(data: str, first: str = "mul(", second: str = ",", third: str = ")") -> list[str]:
    valid = []
    for i in range(len(data)):
        if data[i: i+4] == first:
            if second in data[i+4: i+8] and third in data[i+5: i+12]:
                end_index = data.find(third, i, i+12)
                valid.append(data[i+4: end_index])
        if i == len(data) - 8:
            break
    return valid

# function to calculate results of multiplications
def multiply(data: list[str], separation: str) -> int:
    results = 0
    for list in data:
        num1, num2 = list.split(separation)
        if num1.isalnum and num2.isalnum:   # checking if the pair only contain digits
            if len(num1) <= 3 and len(num2) <=3:
                results += int(num1)*int(num2)
    return results


print(f"Results of valid multiplications:\n{multiply(validation(data), ",")}")