n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)
x,y=0,0
def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
b=groupby(a)
l=len(b)
for i in range(l):
    if x==0:
        if b[i][1]>=4:
            x,y=b[i][0],b[i][0]
        elif b[i][1]>=2:
            x=b[i][0]
    elif y==0:
        if b[i][1]>=2:
            y=b[i][0]
    else:
        break
print(x*y)
