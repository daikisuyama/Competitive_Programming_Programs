#たかだか道を全て回るくらいの計算量
#パス保存したい？
#使えなくする工夫は？
#最短閉路も部分的に最短経路に似た性質をもつ
#最短閉路であっても最短経路に落として考えれば良い→どうするか？
#最初と最後は必ず1→k,l→1の移動があるので、その移動を除いた
#WFはPyPyでだす
n,m=map(int,input().split())
edges=[list(map(int,input().split())) for i in range(m)]
inf=100000000000
wf=[[inf]*n for i in range(n)]
for i in range(n):
    wf[i][i]=0
for i in range(m):
    wf[edges[i][0]-1][edges[i][1]-1]=edges[i][2]
    wf[edges[i][1]-1][edges[i][0]-1]=edges[i][2]
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            wf[j][k]=min(wf[j][i]+wf[i][k],wf[j][k])

mi=inf
for i in range(1,n):
    for j in range(i+1,n):
        mi=min(mi,wf[0][i]+wf[i][j]+wf[j][0])
if mi==inf:
    print(-1)
else:
    print(mi)