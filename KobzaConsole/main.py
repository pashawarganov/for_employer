import random
from colorama import init, Fore

vocb =""    #словник
name ="vocabulary"
with open(f"{name}.txt", encoding="utf8") as file: # зчитуємо слова з файлу
    vocb=file.read().split(" ")

wordPC=vocb[random.randint(0, len(vocb)-1)].upper() # загадується слово
#print(wordPC)


check=6 #кількість спроб
print("Гра \"Кобза\"")

while check>0:
    ifA=False      

    while not ifA :
        wordPl=input(Fore.WHITE+"Введіть ваше слово =").upper()

        if len(wordPl)==5 and wordPl in vocb: #перевірка що слово має 5 літер і є у словнику
            ifA=True
        else:
            print("Невірно введене слово!!!")

    i=0                     #щоб рахувати яку літеру перевіряю
    correct=0               #кількість правильно вгаданих букв

    for j in wordPl:            #Перевірка чи правильно введено слово по буквам
        ifIn=False
        if wordPC[i]==j:        #Перевірка на букву на тому самому місці
            print(Fore.GREEN+j)
            correct+=1

        else:

            for n in wordPC:
                if n==j:        #Перевірка на букву на іншому місці
                    ifIn=True
            if ifIn:
                print(Fore.YELLOW+j)
            else:
                print(Fore.WHITE + j)

        i+=1

    if correct==5:      
        print(Fore.WHITE+"Так! Вірно!") #Перемога
        break

    check -= 1

    print(Fore.RED + f"Спроб залишилось = {check}")
else:
    print(Fore.RED +"На жаль ви програли(")     #Поразка
    print(Fore.GREEN+f"Правильне слово={wordPC}")