import matplotlib.pyplot as plt

x = [1,2,3,4]

rahul = [60,70,80,90]
aman = [55,65,85,95]

plt.plot(x, rahul, label="Rahul")
plt.plot(x, aman, label="Aman")

plt.legend()

plt.show()