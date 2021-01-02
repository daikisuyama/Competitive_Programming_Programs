n,m=map(int,input().split())
x=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    x[a].append(b)
    x[b].append(a)

for i in range(n):
    sorted(set(x[i]),key=x[i].index)

for i in range(n):
    l=len(x[i])
    check=[0]*n
    check[i]=-1
    for j in range(l):
        check[x[i][j]]=-1
        m=len(x[x[i][j]])
        for k in range(m):
            if check[x[x[i][j]][k]]!=-1:
                check[x[x[i][j]][k]]=1
    print(check.count(1))
    #print(check)
