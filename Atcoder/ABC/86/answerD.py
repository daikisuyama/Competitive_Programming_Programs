n,k=map(int,input().split())
g=[[[0,0] for i in range(k)] for j in range(k)]

for i in range(n):
    x,y,c=input().split()
    x,y=int(x),int(y)
    if y%(2*k)<k and x%(2*k)<k:
        g[y%(2*k)][x%(2*k)][c=="W"]+=1
    elif y%(2*k)<k:
        g[y%(2*k)][x%(2*k)-k][c=="B"]+=1
    elif x%(2*k)<k:
        g[y%(2*k)-k][x%(2*k)][c=="B"]+=1
    else:
        g[y%(2*k)-k][x%(2*k)-k][c=="W"]+=1

ac=[[[0]*(k+1) for i in range(k+1)] for l in range(2)]
for l in range(2):
    for i in range(k):
        for j in range(k):
            ac[l][i+1][j+1]=ac[l][i][j+1]+ac[l][i+1][j]-ac[l][i][j]+g[i][j][l]

ans=0
for i in range(k):
    for j in range(k):
        ans=max(ac[0][k][k]-ac[0][i][k]-ac[0][k][j]+2*ac[0][i][j]+ac[1][i][k]+ac[1][k][j]-2*ac[1][i][j],ans)
        ans=max(ac[1][k][k]-ac[1][i][k]-ac[1][k][j]+2*ac[1][i][j]+ac[0][i][k]+ac[0][k][j]-2*ac[0][i][j],ans)
print(ans)