n,m,q=map(int,input().split())
scores=[[0]*m for i in range(n)]
questions=[n]*m
for i in range(q):
    s=list(map(int,input().split()))
    if s[0]==1:
        ans=0
        for i in range(m):
            if scores[s[1]-1][i]:
                ans+=questions[i]
        print(ans)
    else:
        questions[s[2]-1]-=1
        scores[s[1]-1][s[2]-1]=1