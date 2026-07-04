import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("mini_project/student.csv")
sns.histplot(df["Marks"],kde=True)
plt.title("distributed of makrs")
plt.show()
