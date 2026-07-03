data = [
    "Rahul,5000,120,Tech",
    "Priya,12000,350,Fashion",
    "Aman,8000,220,Travel",
    "Riya,15000,400,Fashion"
]

people = []

for row in data:
    x = row.split(",")

    x[1] = int(x[1])
    x[2] = int(x[2])

    people.append(x)

print(people)