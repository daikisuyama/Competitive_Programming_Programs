n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
cd=[list(map(int,input().split())) for i in range(m)]

def manh(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

ans=[]
for i in range(n):
    ans_sub=[0,manh(ab[i],cd[0])]
    for j in range(m):
        k=manh(ab[i],cd[j])
        if k<ans_sub[1]:
            ans_sub=[j,k]
    ans.append(ans_sub[0])
for i in range(n):
    print(ans[i]+1)
