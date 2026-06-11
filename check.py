import pandas as pd

df = pd.read_csv(
    r"C:\Users\PragatheeshIndiran\Downloads\child_chunks_202606111320.csv"
)

print(df.columns.tolist())
print(df.head())