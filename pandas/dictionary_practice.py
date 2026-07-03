friends = {
    "Subodh": ["Rahul", "Aman"],
    "Rahul": ["Subodh", "Priya"],
    "Aman": ["Subodh", "Riya"],
    "Priya": ["Rahul"],
    "Riya": ["Aman"]
}

person = "Subodh"

recommend = []

for friend in friends[person]:
    for fof in friends[friend]:

        if fof != person and fof not in friends[person]:
            if fof not in recommend:
                recommend.append(fof)

print("People You Might Know")
print(recommend)