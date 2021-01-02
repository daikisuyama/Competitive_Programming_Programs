#×
#and1,or0は決まる
from sys import exit
n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
u=list(map(int,input().split()))
v=list(map(int,input().split()))
a=[[[-1]*64 for i in range(n)] for j in range(n)]
for i in range(n):
    if s[i]==0:
        for j in range(64):
            if (u[i]>>j)&1:
                for k in range(n):
                    if a[i][k][j]!=0:
                        a[i][k][j]=1
                    else:
                        print(-1)
                        exit()
    else:
        for j in range(64):
            if not((u[i]>>j)&1):
                for k in range(n):
                    if a[i][k][j]!=1:
                        a[i][k][j]=0
                    else:
                        print(-1)
                        exit()
for i in range(n):
    if t[i]==0:
        for j in range(64):
            if (u[i]>>j)&1:
                for k in range(n):
                    if a[k][i][j]!=0:
                        a[k][i][j]=1
                    else:
                        print(-1)
                        exit()
    else:
        for j in range(64):
            if not((u[i]>>j)&1):
                for k in range(n):
                    if a[k][i][j]!=1:
                        a[k][i][j]=0
                    else:
                        print(-1)
                        exit()
r=True
ans=[[] for i in range(n)]
for i in range(n):
    for j in range(n):
        ans_=0
        for k in range(64):
            if a[i][j][k]==-1:
                if r:
                    a[i][j][k]=1
                else:
                    a[i][j][k]=0
                r=False
                ans_+=((2**k)*a[i][j][k])
        ans[i].append(ans_)
for i in range(n):
    print(" ".join(map(str,ans[i])))


