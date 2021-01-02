n=int(input())
a=[int(input())-1 for i in range(n)]
now=0
x=[0]*n
i=0
while x[now]==0:
    i+=1
    x[now]=1
    now=a[now]
    if now==1:
        print(i)
        break
else:
    print(-1)
