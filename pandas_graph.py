import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mini_project/student.csv")

print(df)

plt.figure(figsize=(8,5))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.grid(axis="y")

plt.show()