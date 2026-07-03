import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
plt.plot([1,2,3],[2,4,6])
plt.title("Line")

plt.subplot(2, 2, 2)
plt.bar(["A","B","C"], [3,5,2])
plt.title("Bar")

plt.subplot(2, 2, 3)
plt.pie([40,35,25], labels=["A","B","C"])
plt.title("Pie")

plt.subplot(2, 2, 4)
plt.scatter([1,2,3],[5,3,6])
plt.title("Scatter")

plt.tight_layout()

plt.show()