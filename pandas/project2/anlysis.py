people = [
    ['Rahul',5000,120,'Tech'],
    ['Priya',12000,350,'Fashion'],
    ['Aman',8000,220,'Travel'],
    ['Riya',15000,400,'Fashion']
]

mx_follow = people[0]

for person in people:
    if person[1] > mx_follow[1]:
        mx_follow = person

print("Top Follower:")
print(mx_follow)

mx_post = people[0]

for person in people:
    if person[2] > mx_post[2]:
        mx_post = person

print("Top Posts:")
print(mx_post)

count = {}

for person in people:
    category = person[3]

    if category not in count:
        count[category] = 1
    else:
        count[category] += 1

print("Category Count:")
print(count)

total_follow = 0

for person in people:
    total_follow += person[1]

avg_follow = total_follow / len(people)

print("Average Followers:")
print(avg_follow)

total_post = 0

for person in people:
    total_post += person[2]

avg_post = total_post / len(people)

print("Average Posts:")
print(avg_post)