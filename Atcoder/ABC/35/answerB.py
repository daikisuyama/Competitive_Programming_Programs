s=input()
t=int(input())

x=[0 for i in range(3)]
for i in s:
    if i=="L":
        x[0]-=1
    elif i=="R":
        x[0]+=1
    elif i=="U":
        x[1]+=1
    elif i=="D":
        x[1]-=1
    else:
        x[2]+=1

#ここの条件判定しっかり
y=abs(x[0])+abs(x[1])
if t==1:
    print(y+x[2])
else:
    if y >= x[2]:
        print(y-x[2])
    else:
        x[2]-=y
        print(x[2]%2)
