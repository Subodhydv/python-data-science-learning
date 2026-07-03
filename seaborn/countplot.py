import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai", "Delhi", "Patna", "Mumbai"]
})

sns.countplot(x="City", data=df)

plt.title("Students by City")
plt.show()