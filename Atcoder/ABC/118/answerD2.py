n,m=map(int,input().split())
x=[2,5,5,4,5,6,3,7,6]
a=[]
for i in map(int,input().split()):
    a.append([i,x[i-1]])
a.sort(reverse=True)
dp=[0]*(n+1)
for i in range(m):
    for j in range(n+1):
        if j==0 or dp[j]!=0:
            if j+a[i][1]<=n:
                dp[j+a[i][1]]=max(dp[j+a[i][1]],dp[j]*10+a[i][0])
print(dp[n])