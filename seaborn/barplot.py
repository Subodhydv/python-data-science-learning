import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("mini_project/student.csv")

sns.barplot(x="Department", data=df)

plt.title("Students by Department")

plt.show()