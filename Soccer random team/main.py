import random
import json

with open('teams.json','r' ,encoding="utf8") as f:   # зчитуємо команди з файлу
    all_teams = json.load(f)

def new_team(ex_teams):                            # обираємо команду без повтора
    team = ""
    while (team in ex_teams or team == ""):
        team = all_teams[random.randint(0, len(all_teams)-1)]
    return team

players=["Бодя","Саша","Ваня","Паша"]
teams=[]

print("---------------------------------------------------------")
for i in range(len(players)):
    teams.append(new_team(teams))               # обираємо команду
    print(f"{players[i]} грає {teams[i]}")      # вивід
print("---------------------------------------------------------")

'''
for i in all_teams:
    for j,n in i.items():
        print(j,"***",n)
    print("----")
'''
#print(all_teams[0]["name"])

# Варто зробити JSON файл з масивом об'єктів по командам 
# Кожна команда має ключі: назва, іконка, оцінка і ліга
# Можна зробити словник для виводу. Ключ - гравець, значення - команда.