#11/26 10:15~10:25
#問題文読みにくい
r,c=map(int,input().split())
sen=[list(map(int,input().split())) for i in range(r)]
ans=0
for i in range(2**r):
    ans_sub=0
    for k in range(c):
        now=[sen[l][k] if (i>>l)&1 else 1-sen[l][k] for l in range(r)]
        ans_sub+=max(sum(now),r-sum(now))
    ans=max(ans,ans_sub)
print(ans)