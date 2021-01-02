import queue
n=int(input())
#最短の長さ、何通りか
a,b=map(int,input().split())
dp=[0]*n
dp[a-1]= 1
check=[[0]*n for i in range(n)]
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    check[x-1][y-1]=1
    check[y-1][x-1]=1

q=queue.Queue()
q.put(a-1)
while not q.empty():
    l=q.qsize()
    dp_sub=[0]*n
    for i in range(l):
        g=q.get()
        for j in range(n):
            if check[g][j]==1 and dp[j]==0:
                dp_sub[j]+=dp[g]
    for i in range(n):
        if dp[i]==0 and dp_sub[i]!=0:
            dp[i]=dp_sub[i]
            q.put(i)

print(dp[b-1]%(10**9+7))
