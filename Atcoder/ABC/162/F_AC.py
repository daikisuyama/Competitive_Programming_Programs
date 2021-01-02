n=int(input())
a=list(map(int,input().split()))
minf=-10000000000000
x=[[0,0,0] for i in range(n)]
x[0]=[0,0,a[0]]
for i in range(n-1):
    if i%2==0:
        x[i+1]=[max(x[i][0],x[i][1]),x[i][2],x[i][0]+a[i+1]]
    else:
        x[i+1]=[max(x[i][1],x[i][2]),x[i][0]+a[i+1],x[i][1]+a[i+1]]
print(max(x[-1][1],x[-1][2]) if n%2==0 else max(x[-1][0],x[-1][1]))
