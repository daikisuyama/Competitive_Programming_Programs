n,m=map(int,input().split())
x=[0]*n
for i in range(m):
    y,z=map(int,input().split())
    x[y-1]+=1
    x[z-1]+=1
for i in range(n):
    print(x[i])
