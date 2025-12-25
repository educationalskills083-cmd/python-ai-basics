# Simple AI-like decision system

def recommend_career(skill):
    if skill == "python":
        return "You should explore AI and automation"
    elif skill == "design":
        return "You should explore UI/UX"
    else:
        return "Explore general programming"

user_skill = "python"
print(recommend_career(user_skill))
