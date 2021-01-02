from sys import exit
s=input()
xy=list(map(int,input().split()))

def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
s=groupby(s)
ab=[[],[]]
turn=True
#初めまっすぐの場合
if s[0][0]=="F":
    xy[0]-=s[0][1]
    s.pop(0)
for i in s:
    if i[0]=="F":
        ab[not turn].append(i[1])
    elif i[1]%2==1:
        turn=not turn
for i in range(2):
    ab[i].sort(reverse=True)
    for j in ab[i]:
        xy[i]=abs(xy[i])-abs(j)
    if xy[i]!=0:
        print("No")
        exit()
print("Yes")