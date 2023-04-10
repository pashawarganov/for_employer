def Get_p(x1,x2,n): #функція для прорахунку р
    if x1>x2:
        a = (x1 - x2) % n
    else:
        a = (x1 - x2 + n) % n
    while a>0 and n>0: #алгоритм Евкліда/знаходження НСК - найбільшого спільного дільника
        if n>a:
            n=n-a
        else:
            a=a-n
    return n

def Get_q(n): #функція знаходження q
    arrX = [2] #масив значень Х
    p = 0
    i = 1 #змінна для перебору масиву
    ifA=True #умова що співпадіння не було
    print("x 0 =",arrX[0]) #вивід нульового елементу
    while ifA: #перебір масиву
        arrX.append(0) #додаю пустий елемент у масив
        arrX[i]=(arrX[i-1]**2+1)%n #рахую Х-іте
        print ("x",i,"=",arrX[i])
        j=0 #змінна для перебору вкладеного масиву
        while j<i: #цикл для визначення Х що співпали
            if arrX[i]==arrX[j]:
                print("x", i, "та", "x", j, "співпали")
                p = Get_p(arrX[i - 1], arrX[j - 1], n)
                ifA=False
            j+=1
        i+=1
    print("p =", p)
    print("q=", n // p)

def Get_Phi(n):
    i=2
    result=n
    while i*i<n:
        if n%i ==0:
            while n%i ==0:
                n/=i
            result-=result/i
        i += 1
    if n>1:
        result -= result / n
    return int(result)

def Get_d(n,e): #функція для прорахунку d
    d=0
    Phi1 = int(Get_Phi(n))
    Phi2 = int(Get_Phi(Phi1))
    d=int((e**(Phi2-1))%Phi1) #не прауює бо занадто великі числа
    return d

def __main__():
    print("Лабораторна робота №5 з криптоаналізу")
    C=int(input("Введіть C="))
    e=int(input("Введіть e="))
    n=int(input("Введіть n="))
    Get_q(n)
    d=Get_d(n,e)
    print("d=",d)
    M = int(C ** d % n)
    print("M=", M)
    if C==M**e%n:
        print("Перевірка пройшла успішно")
    else:
        print("Щось пішло не так")

#Перевірочні значення(2 варіант)
#C=10113
#e=247
#n=49949
#p=199
#q=251
#d=41083
#M=119
__main__()