n,m,q=map(int,input().split())
Q=[list(map(int,input().split())) for i in range(q)]
ans=0

R=[range(i,m) for i in range(m)]
def dfs(s,d,l):
    global n,m,Q,ans
    if d==n:
        ans_=0
        for k in Q:
            a,b,c,e=k
            if int(s[b-1])-int(s[a-1])==c:
                ans_+=e
        ans=max(ans,ans_)
    else:
        for i in R[l]:
            dfs(s+str(i),d+1,i)
dfs("",0,0)

print(ans)