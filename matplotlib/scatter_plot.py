import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 75, 90]

plt.scatter(hours, marks)

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.grid(True)

plt.show()