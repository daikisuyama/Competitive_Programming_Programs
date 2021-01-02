n=int(input())
ng={int(input()) for i in range(3)}
if n in ng:
    print("NO")
    exit()
#回数も
inf=100000000000
dp=[inf]*(n+1)
dp[n]=0
#0,1間違えて草
for i in range(n,0,-1):
    if dp[i]!=inf:
        for j in range(max(i-3,0),i):
            if j not in ng:
                dp[j]=min(dp[j],dp[i]+1)
print("YES" if dp[0]<=100 else "NO")