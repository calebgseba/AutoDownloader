import pandas as pd

# Simple way to read the first cell
df = pd.read_excel("PureData.xlsx")
first_cell = df.iloc[0, 0]  # Row 0, Column 0 (first cell)
print(f"First cell value: {first_cell}")

# Alternative simple way
first_cell_alt = df.iloc[0][0]
print(f"First cell value (alternative): {first_cell_alt}")

# Show what's in the first few cells
print(f"\nFirst row: {df.iloc[0].values}")
print(f"First column: {df.iloc[:, 0].values}")










