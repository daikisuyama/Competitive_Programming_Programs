from sys import setrecursionlimit
setrecursionlimit(10**7)
n=int(input())
a,b,c=[],[],[]
for i in range(n):
    x,y,z=map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(z)
tree=[[] for i in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
if sum(b)!=sum(c):
    print(-1)
    exit()


check=[False]*n
check[0]=True
#値を単調減少に
def dfs(i,m):
    global tree,check,b,c,a
    for j in tree[i]:
        if not check[j]:
            check[j]=True
            a[j]=min(a[j],m)
            dfs(j,a[j])
dfs(0,a[0])
#下から貪欲に
ans=[10000000000000]*n
check=[False]*n
check[0]=True
def dfs(i):
    global tree,ans,b,c,a
    ret=0
    now=[(b[i]==0 and c[i]==1),(b[i]==1 and c[i]==0)]
    for j in tree[i]:
        if not check[j]:
            check[j]=True
            d=dfs(j)
            ret+=ans[j]
            now[0]+=d[0]
            now[1]+=d[1]
    ret+=(min(now)*a[i]*2)
    ans[i]=ret
    return [now[0]-min(now),now[1]-min(now)]
dfs(0)
print(ans[0])