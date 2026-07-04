import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("mini_project/student.csv")

sns.scatterplot(x="Age", y="Marks", data=df)

plt.title("Age vs Marks")

plt.show()