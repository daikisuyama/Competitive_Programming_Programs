#11/28 12:22~
n,w=map(int,input().split())
dp=[-1]*(w+1)
dp[0]=0
for i in range(n):
    v,w_=map(int,input().split())
    for j in range(w):
        if dp[j]!=-1:
            if j+w_<=w:
                dp[j+w_]=max(dp[j+w_],dp[j]+v)
print(max(dp))