n=int(input())
x=list(map(int,input().split()))
x.sort()
y=[]
for i in range(x[0],x[-1]+1):
    su=0
    for j in range(n):
        su+=((x[j]-i)**2)
    y.append(su)
print(min(y))
