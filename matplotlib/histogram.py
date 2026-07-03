import matplotlib.pyplot as plt

marks = [45, 52, 60, 61, 63, 70, 71, 72, 75, 80, 82, 85, 90, 92, 95]

plt.hist(marks,bins=10)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(True)

plt.show()