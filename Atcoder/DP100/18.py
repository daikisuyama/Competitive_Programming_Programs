n,p=map(int,input().split())
item=[list(map(int,input().split())) for i in range(n)]
item.sort(reverse=True)
dp=[0]*(p+1+100)
for i in range(n):
    a,b=item[i]
    for j in range(p,-1,-1):
        dp[j+a]=max(dp[j+a],dp[j]+b)
print(max(dp))
#print(dp)