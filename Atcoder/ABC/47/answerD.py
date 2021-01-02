n,t=map(int,input().split())
a=list(map(int,input().split()))
x=[0]*n
x[0]=a[0]
for i in range(1,n):
    x[i]=min(x[i-1],a[i])
d=dict()
for i in range(1,n):
    y=a[i]-x[i-1]
    if y>0:
        if y in d:
            d[y]+=1
        else:
            d[y]=1
d=list(d.items())
d.sort(reverse=True)
print(d[0][1])