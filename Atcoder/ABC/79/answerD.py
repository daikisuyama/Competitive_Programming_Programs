h,w=map(int,input().split())
WF=[list(map(int,input().split())) for i in range(10)]
a=[list(map(int,input().split())) for i in range(h)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            WF[i][j]=min(WF[i][j],WF[i][k]+WF[k][j])

ans=0
for i in range(h):
    for j in range(w):
        if a[i][j]!=-1:
            ans+=WF[a[i][j]][1]
print(ans)
