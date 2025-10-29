import pandas as pd

count = 1

df = pd.read_excel("PureData.xlsx")
first_cell = df.iloc[0, 0]
print(first_cell)
print("You are on cell", count + 3)