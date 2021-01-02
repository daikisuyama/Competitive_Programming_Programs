n=int(input())
c=[[0]*n for i in range(n)]
ans=[[n]*n for i in range(n)]
p=list(map(int,input().split()))
for i in range(n**2):
    if i//n==0 or i//n==n-1 or i%n==0 or i%n==n-1:
        ans[i//n][i%n]=0
    q=p[i]-1
    c[q//n][q%n]=i

def dfs(i,j):
    global c,ans,n
    


for i in range(n):
    dfs(0,i)
    dfs(n-1,i)
    if i!=0:
        dfs(i,0)
    if i!=n-1:
        dfs(i,n-1)
