likes = {
    "Subodh": ["Cricket", "AI"],
    "Rahul": ["Cricket", "Python"],
    "Aman": ["Football", "Python"],
    "Priya": ["Machine Learning"],
    "Riya": ["AI", "Movies"]
}

recommend_pages = set()

for person in likes:
    if person != "Subodh":
        for page in likes[person]:
            if page not in likes["Subodh"]:
                recommend_pages.add(page)

print("Pages You Might Like")
print(recommend_pages)