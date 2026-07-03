import matplotlib.pyplot as plt

dept = ["CSE", "ECE", "ME"]
students = [5, 3, 2]

plt.pie(students, labels=dept, autopct="%1.1f%%")

plt.title("Department Distribution")

plt.show()