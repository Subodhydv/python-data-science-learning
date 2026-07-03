import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 5, 8, 12, 15]

plt.plot(
    x,
    y,
    marker="o",
    color="red",
    linestyle="--"
)

plt.title("My First Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)

plt.show()