from sys import exit
s=input()
x,y=map(int,input().split())

def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
s=groupby(s)
a,b=[],[]
turn=True
#初めまっすぐの場合
if s[0][0]=="F":
    x-=s[0][1]
    s.pop(0)
for i in s:
    if i[0]=="F":
        if turn:
            a.append(i[1])
        else:
            b.append(i[1])
    else:
        if i[1]%2==1:
            turn=not turn
a.sort(reverse=True)
b.sort(reverse=True)
for i in a:
    if x>0:
        x-=i
    else:
        x+=i
for i in b:
    if y>0:
        y-=i
    else:
        y+=i
if x!=0 or y!=0:
    print("No")
else:
    print("Yes")