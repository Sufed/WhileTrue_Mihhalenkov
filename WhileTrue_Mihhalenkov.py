#1
for i in range(2, 12, 3):
    print(i, end=" ")
print()
for i in range(12, 2, -2):
    print(i, end=" ")
print()
#2.1
print("Arvuta peast! ...4*100-55")
o_vastus=4*100-55
vastus=int(input("Lahenda �lesanne..."))
k=1
while vastus!=o_vastus:
    print("Viga! Sisesta �ige vastus...", )
    break
    vastus=int(input("Sisesta vastus..."))
    k+=1
print("�ige vastus! Katsed oli ...",k )
#2.2
x=0
while x<30:
    if x%2==1:
        print(x, end=" ")
    x+=1
