n,m=map(int,input().split())
inf=100000000
wf=[[inf]*n for i in range(n)]
wf_sub=[[inf]*n for i in range(n)]
for i in range(n):
    wf[i][i]=0
    wf_sub[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    wf[a-1][b-1]=c
    wf_sub[a-1][b-1]=c
    wf[b-1][a-1]=c
    wf_sub[b-1][a-1]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            wf[i][j]=min(wf[i][j],wf[i][k]+wf[k][j])
cnt=0
for i in range(n):
    for j in range(n):
        if wf_sub[i][j]!=0 and wf_sub[i][j]!=inf:
            if wf[i][j]!=wf_sub[i][j]:
                cnt+=1

print(cnt//2)
