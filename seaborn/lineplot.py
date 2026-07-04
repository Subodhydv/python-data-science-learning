import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 180, 170, 200]
})

sns.lineplot(x="Month", y="Sales", data=df)

plt.title("Monthly Sales")

plt.show()