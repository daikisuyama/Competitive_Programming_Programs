n,m,q=map(int,input().split())
graph=[[0 if i!=j else 1 for i in range(n)] for j in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u-1][v-1]=1
    graph[v-1][u-1]=1
color=list(map(int,input().split()))
for i in range(q):
    s=list(map(int,input().split()))
    if s[0]==1:
        x=s[1]-1
        print(color[x])
        for j in range(n):
            if graph[x][j]:
                color[j]=color[x]
    else:
        x,y=s[1]-1,s[2]
        print(color[x])
        color[x]=y