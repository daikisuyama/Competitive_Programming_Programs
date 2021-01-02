import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    ans=[[0]*m for i in range(n)]
    d=dict()
    for i in range(n):
        l1=list(map(int,input().split()))
        for j in range(m):
            d[l1[j]]=[-1,j]
    for i in range(m):
        l2=list(map(int,input().split()))
        for j in range(n):
            d[l2[j]][0]=j
    for i in d:
        ans[d[i][0]][d[i][1]]=i
    for i in range(n):
        print(" ".join(map(str,ans[i])))