n,k=map(int,input().split())
x=list(map(int,input().split()))
t=input()
y=[[] for i in range(k)]
for i in range(n):
    if t[i]=="r":
        y[i%k].append(2)
    elif t[i]=="s":
        y[i%k].append(0)
    else:
        y[i%k].append(1)

def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
c=0
for i in range(k):
    z=groupby(y[i])
    l=len(z)
    for j in range(l):
        c+=(x[z[j][0]]*((z[j][1]+1)//2))
print(c)
