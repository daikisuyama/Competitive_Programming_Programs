n,k,s,t=map(int,input().split())
b=list(map(int,input().split()))
a=[]
for i in range(n):
    for j in range(18):
        if (s>>j)&1 and not((b[i]>>j)&1):
            break
    else:
        for j in range(18):
            if not((t>>j)&1) and (b[i]>>j)&1:
                break
        else:
            a.append(b[i])
n=len(a)
k=min(n,k)
#dp[i] i個選んだ時に(S,T)となるのが何通り存在するか(Sが論理積でTが論理和)
#1-indexed
dp=[{(s,t):0} for i in range(k)]
for i in range(n):
    dp_sub=[dict() for i in range(k)]
    dp_sub[0][(a[i],a[i])]=1
    for j in range(k-1):
        for l in dp[j]:
            m=(l[0]&a[i],l[1]|a[i])
            if m in dp_sub[j+1]:
                dp_sub[j+1][m]+=dp[j][l]
            else:
                dp_sub[j+1][m]=dp[j][l]
    for j in range(k):
        for l in dp_sub[j]:
            if l in dp[j]:
                dp[j][l]+=dp_sub[j][l]
            else:
                dp[j][l]=dp_sub[j][l]
print(sum([dp[i][(s,t)] for i in range(k)]))