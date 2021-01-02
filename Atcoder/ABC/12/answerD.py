n,m=map(int,input().split())
inf=10000000000
wf=[[inf]*n for i in range(n)]
for i in range(n):
    wf[i][i]=0
for i in range(m):
    a,b,t=map(int,input().split())
    wf[a-1][b-1]=t
    wf[b-1][a-1]=t
for i in range(n):
    for j in range(n):
        for k in range(n):
            wf[j][k]=min(wf[j][i]+wf[i][k],wf[j][k])
ans=inf
for i in range(n):
    ans=min(ans,max(wf[i]))
print(ans)