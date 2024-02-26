from tkinter import *
import random
import json


root=Tk()
root.title("Вибір команди")
root.geometry("700x300")
windowIcon=PhotoImage(file='icons/sportArea.png')
root.iconphoto(0,windowIcon)

with open('teams.json','r' ,encoding="utf8") as f:   # зчитуємо команди з файлу
    all_teams = json.load(f)
for i in all_teams:             #Змінюю розташування іконок і рейтингу на іконка зображення
    i['icon']=PhotoImage(file=i['icon'])
    i['ratingico']=PhotoImage(file=i['ratingico'])

players=["Бодя","Саша","Ваня","Паша"]
checkmark=["5","4,5","4","3,5","3"]

def new_team(ex_teams):                            # обираємо команду без повтора
    team = ""
    while (team in ex_teams or team == "" or team['rating'] not in checkmark):
        team = all_teams[random.randint(0, len(all_teams)-1)]
        #if team['rating']!="4":
        #    team=""
    return team

def com1():              #Функція, що запускається при натисканні кнопки вибору команд
    teams=[]
    for i in range(len(players)):
        teams.append(new_team(teams))                           # обираємо команду
        team_name[i].config(text=f"{players[i]} грає {teams[i]['name']}\t") # вивід тексту
        icons[i].config(image=teams[i]['icon'])         #вивід іконки
        rating[i].config(image=teams[i]['ratingico'])      #виід рейтингу команди картинкою
        league[i].config(text=teams[i]['league'])
        #print(nBox)

def com2():              #Функція, що запускається при натисканні кнопки зберегти
    with open("teams.txt", 'w', encoding="utf8") as file: 
        for i in range(len(players)):
            file.write(team_name[i]['text']+"\n")

def com3():              #Функція, що запускається при натисканні кнопки показати
    with open("teams.txt", encoding="utf8") as file:
        s=file.read().split("\n")
        for i in range(len(players)):
            team_name[i].config(text=s[i])
            

mainButton=Button(text="Вибрати команди",font=20, command=com1)      #Кнопка, що запускає вибір команд
mainButton.grid(row=0, column=1, sticky=W)
saveButton=Button(text="Зберегти",font=20, command=com2)      #Кнопка, що записує команди
saveButton.grid(row=6, column=1, sticky=W)
showButton=Button(text="Показати",font=20, command=com3)      #Кнопка, що показує записані команди
showButton.grid(row=6, column=2, sticky=W)

header = Label(text="Обрані команди:",font=20,anchor=CENTER)      #Просто заголовок, що вказує, де будуть обрані команди
header.grid(row=1, column=1, sticky=W)

skips=[]                #Поле для запису скіпів
team_name=[]            #Текст в який записуються назви обраних команд
league=[]                #Текст в який записуються ліги обраних команд
icons=[]                #Рамка в яку вставляється зображення
rating=[]               #Рамка для рейтингу команди
ball_icon = PhotoImage(file='icons/ball.png')     #Іконка м'яча
startRating_icon = PhotoImage(file='icons/0stars.png')      #Іконка нульвого рейтингу

for i in range(len(players)):
    skips.append(Entry(width = 5))
    skips[i].grid(row=2+i, column=0, sticky=W)
    team_name.append(Label(text="Натисніть кнопку, щоб обрати команди",font=16)) 
    team_name[i].grid(row=2+i, column=2, sticky=W)
    icons.append(Label(image=ball_icon))                 
    icons[i].grid(row=2+i, column=1, sticky=W)
    rating.append(Label(image=startRating_icon))
    rating[i].grid(row=2+i, column=3, sticky=W)
    league.append(Label(text="Ліга",font=16)) 
    league[i].grid(row=2+i, column=4, sticky=W)
'''
nBox2 = StringVar()


nBox=[]
for i in range(len(checkmark)):
    nBox.append("0")
    Box1_checkbutton = Checkbutton(text=checkmark[i],onvalue=checkmark[i],variable=nBox[i])
    Box1_checkbutton.grid(row=7+i, column=0, sticky=W)
'''


mainloop()
'''
Зробити щоб скіпи виводились на кнопку і віднімались там же
В майбутньому ще треба ввести фільтри по оцінці і лізі. 
    - Як правильно зробити чекбокси?
Також варто зробити так, щоб текст не пригав

Тотально переробити прогу зробивши кілька форм(вибір команд, збережені команди, склад команди і тп)
'''