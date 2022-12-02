from random import randint, choice
from math import sqrt

lista=[]
y=-10

while y<11:
    lista.append(y)
    y+=1

x=choice(lista)
a=randint(2,10)
b=randint(-10,10)

if b>0:
    c=a*x+b
    print("Los ekvationen ",a,"x +",b,"=",c)

elif b<0:
    b1=sqrt(b**2)
    c=a*x-b1
    print("Los ekvationen ",a,"x -",int(b1),"=",int(c))

else:
    c=a*x 
    print("Los ekvationen ",a,"x =",c)

svar=int(input("Vad ar 'x': "))

if svar==x:
    print("Ratt svar")

elif svar!=x:
    print("Fel svar \nRatt svar ar",x)
