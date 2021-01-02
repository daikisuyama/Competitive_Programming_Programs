#二部グラフにできるのか
#ここからよ
#実は奇サイクルを含まない=二部グラフとなる
#それぞれのレベルで奇サイクルかどうか
#二部グラフを考えて残りでもどんどん二部グラフを考えるイメージ
#そんなに難しくないか

#最終的には1or2の状態で残る
N=int(input())
ans=[[0]*N for j in range(N)]
#nはvecの長さ
#次の通路のレベル
def dfs(n,vec,level):
    global ans
    l=vec[:n//2]
    r=vec[n//2:]
    for i in l:
        for j in r:
            ans[i][j]=level
    if len(l)>1:
        dfs(len(l),l,level+1)
    if len(r)>1:
        dfs(len(r),r,level+1)


dfs(N,[i for i in range(N)],1)
for i in range(N-1):
    a=[]
    for j in range(N):
        if i<j:
            a.append(str(ans[i][j]))
    print(" ".join(a))