import math
from colorama import init, Fore

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

# p=809
# a=32
# Y_a=498
# Y_b=565
p=int(input("Введіть p="))
a=int(input("Введіть a="))
Y_a=int(input("Введіть Y_a="))
Y_b=int(input("Введіть Y_b="))

print(Fore.RED + "Лабораторна робота №6 з криптоаналізу")

print(Fore.BLUE+"Крок 1")
n=p-1
print("n =",n)

print(Fore.YELLOW+"Крок 2")
m=int(math.sqrt(n)+0.5)
print("m =",m)

print(Fore.GREEN+"Крок 3")
arrJ=[0]*(m+1)
j=0
while j < len(arrJ):
    arrJ[j]=(a**j)%p
    print("j =", j, "|", "x=", arrJ[j])
    j+=1

print(Fore.RED+"Крок 4")
A=a**(Get_Phi(p)-m)%p
print("A =",A)

print(Fore.BLUE+"Крок 5")
i=1
arrI=0
ifA=True
while ifA:
    arrI=(Y_a*A**i)%p
    print("i =", i, "|", "y=", arrI)
    j=0
    while j < len(arrJ):  # цикл для визначення що значення з 3 і 5 кроку співпали
        if arrI == arrJ[j]:
            print("j", j, "та", "i", i, "співпали")
            ifA = False
            break
        j += 1
    i += 1

print(Fore.YELLOW+"Крок 6")
i-=1
if a**j%p==(Y_a*A**i)%p:
    K_a=(i*m+j)%p
    print("K_a =",K_a)

print(Fore.GREEN+"Крок 7")
K=Y_b**K_a%p
print("K=",K)