# load input file
with open("input.txt", "r") as file:
    report = file.read()

# splitting the report into lists of numbers by the new line
report = report.split("\n")

# splitting the lists into list of lists
report = [row.split(" ") for row in report]

# converting the numbers into integers
report = [[int(x) for x in row] for row in report]

# function to calculate rows that satisfies the requirements
def count_safe_reports(report):
    safe_count = 0
    for row in report:
        if sorted(row) == row or sorted(row, reverse=True) == row:
            counter = 0
            for i in range(len(row)-1):
                if abs(row[i+1] - row[i]) >= 1 and abs(row[i+1] - row[i]) <= 3:
                    counter +=1
                    if counter == len(row)-1:
                        safe_count += 1
    return safe_count


print(f"Number of safe reports: {count_safe_reports(report)}")