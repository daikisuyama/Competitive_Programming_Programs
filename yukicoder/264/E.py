from sys import setrecursionlimit
setrecursionlimit(10**7)
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
tree=[[] for i in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
check=[False]*n
dp=[[0,0] for i in range(n)]

def dfs(i):
    global n,a,b,tree,check,dp
    #頂点iを消さない場合
    dp[i]=[a[i],0]
    for j in tree[i]:
        if not check[j]:
            check[j]=True
            dfs(j)
            dp[i][0]+=max(dp[j][0],dp[j][1])
            dp[i][1]+=max(dp[j][0],dp[j][1]+b[i]+b[j])

check[0]=True
dfs(0)
print(max(dp[0]))