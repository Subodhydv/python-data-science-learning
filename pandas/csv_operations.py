import pandas as pd
df = pd.read_csv("coderofdelhi/student1.csv")
print("Original Data")
print(df)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nFirst 3 Rows")
print(df.head(3))

print("\nStatistics")
print(df.describe())

print("\nAscending by Marks")
print(df.sort_values("Marks"))

print("\nDescending by Marks")
print(df.sort_values("Marks", ascending=False))
print(df.isnull().sum())
print(df.dropna())
print(df.fillna(0))
print(df["Age"] = df["Age"].fillna(df["Age"].mean()))
