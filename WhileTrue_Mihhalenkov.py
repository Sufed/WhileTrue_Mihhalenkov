from random import *
#1
for i in range(2, 12, 3):
    print(i, end=" ")
print()
for i in range(12, 2, -2):
    print(i, end=" ")
print()
#2.1
print("Arvuta peast! ...4*100-55")
o_vastus = 4*100-55
while True:
    vastus = int(input("Lahenda ülesanne ..."))
    if vastus == o_vastus:
        print("Õige vastus! Katsed oli ...", o_vastus)
        break
    else:
        print("Viga! Sisesta Õige vastus on ...", )
        o_vastus+= 1
#2.2
x=0
while x<30:
    if x%2==1:
        print(x, end=" ")
    x+=1
