contests_dict = {}

while True:
    text = input()
    if text == "end of contests":
        break
    text = text.split(":")
    contest = text[0]
    password_for_contest = text[1]
    contests_dict[contest] = password_for_contest

users_dict = {}
while True:
    text2 = input()
    if text2 == "end of submissions":
        break
    text2 = text2.split("=>")
    contest_to_check = text2[0]
    password_to_check = text2[1]
    username = text2[2]
    points = int(text2[3])

    if contest_to_check in contests_dict and password_to_check == contests_dict[contest_to_check]:
        if username not in users_dict:
            users_dict[username] = {}

        if contest_to_check not in users_dict[username]:
            users_dict[username][contest_to_check] = points
        else:
            if users_dict[username][contest_to_check] < points:
                users_dict[username][contest_to_check] = points


best_user = ''
best_score = 0
total_score = 0
for user in users_dict:
    total_score = sum(users_dict[user].values())
    if total_score > best_score:
        best_score = total_score
        best_user = user

print(f"Best candidate is {best_user} with total {best_score} points.")

for i in sorted(users_dict):
    print(i)
    for contest_to_check in users_dict[i]:
        print(f"# {contest_to_check} -> {users_dict[i][contest_to_check]}")

