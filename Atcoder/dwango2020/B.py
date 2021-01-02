mod=10**9+7
n=int(input())
x=[int(i) for i in input().split()]
y=[0]*(n-1)
y[0]=1
for i in range(n-2):
    #print(y)
    for j in range(i+1):
        y[j]*=(i+2)
    y[i+1]=y[i]+i+1
#print(y)
ans=0
for i in range(n-1):
    ans+=((x[i+1]-x[i])*y[i])
    ans%=mod
print(ans)
