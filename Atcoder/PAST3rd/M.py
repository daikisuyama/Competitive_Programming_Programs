import sys
sys.setrecursionlimit(3*(10**5))
n,m=map(int,input().split())
path=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    path[u-1].append(v-1)
    path[v-1].append(u-1)
s=int(input())-1
k=int(input())
t=set(map(lambda x:int(x)-1,input().split()))
ans=2*m
def dfs(paths,last,check,d):
    #pathsはsetで保存
    global path,t,ans,k
    for i in path[last]:
        if i not in paths:
            if i in t:
                if check+1==k:
                    ans=min(ans,d)
                else:
                    dfs(paths|{i},i,check+1,d+1)
            else:
                dfs(paths|{i},i,check,d+1)
        else:
            if d<ans:
                dfs(paths,i,check,d+1)

dfs({s},s,0,0)
print(ans+1)