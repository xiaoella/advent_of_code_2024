"""
Day 1 Part 1
"""

# imports
import pandas as pd
# loading dataframe
df = pd.read_csv("input.csv", sep='\s+', header=None, names=["first", "second"])

# sorting first column
first = df["first"].sort_values(ascending=True, ignore_index=True)
# sorting second column
second = df["second"].sort_values(ascending=True, ignore_index=True)
# replacing the dataframe with sorted columns
df = pd.concat([first, second], axis=1)
# creating a new column for absolute differences between the two columns
df["diff"] = abs(df["first"] - df["second"])

# output
print(f"Total distance between lists: {df["diff"].sum()}")


"""
Part 2
"""

# creating a new column with similarity score
df["similarity"] = df.apply(lambda row: (row["first"] == df["second"]).sum() * row["first"], axis=1)

# output
print(f"Similarity score: {df['similarity'].sum()}")