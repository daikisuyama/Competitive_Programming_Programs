#input高速化で通った
#だいぶ血迷った
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[[int(j) for j in input()[:-1]] for i in range(n)]
if n>=4 and m>=4:
    print(-1)
    exit()
if n==1 or m==1:
    print(0)
    exit()
inf=10000000000000
if n==2 or m==2:
    bitcheck=[[0]*4 for i in range(4)]
    for j in range(4):
        for k in range(4):
            for i in range(1):
                if (((j>>i)&1)+((k>>i)&1)+((j>>(i+1))&1)+((k>>(i+1))&1))%2==0:
                    bitcheck[j][k]=False
                    break
            else:
                bitcheck[j][k]=True
    bitcalc=[[0]*4 for i in range(4)]
    for j in range(4):
        for k in range(4):
            for i in range(2):
                if ((j>>i)&1)^((k>>i)&1):
                    bitcalc[j][k]+=1
    if n==2:
        n,m=m,n
        b=[list(x) for x in zip(*a)]
    else:
        b=[i for i in a]
    dp=[[inf]*4 for i in range(n)]
    for i in range(n):
        if i!=0:
            for j in range(4):
                for k in range(4):
                    if bitcheck[j][k]:
                        dp[i][k]=min(dp[i][k],dp[i-1][j]+bitcalc[b[i][0]+b[i][1]*2][k])
        else:
            for k in range(4):
                dp[i][k]=bitcalc[b[i][0]+b[i][1]*2][k]
    print(min(dp[n-1]))
    exit()
if n==3 or m==3:
    bitcheck=[[0]*8 for i in range(8)]
    for j in range(8):
        for k in range(8):
            for i in range(2):
                if (((j>>i)&1)+((k>>i)&1)+((j>>(i+1))&1)+((k>>(i+1))&1))%2==0:
                    bitcheck[j][k]=False
                    break
            else:
                bitcheck[j][k]=True
    bitcalc=[[0]*8 for i in range(8)]
    for j in range(8):
        for k in range(8):
            for i in range(3):
                if ((j>>i)&1)^((k>>i)&1):
                    bitcalc[j][k]+=1
    if n==3:
        n,m=m,n
        b=[list(x) for x in zip(*a)]
    else:
        b=[i for i in a]
    dp=[[inf]*8 for i in range(n)]
    for i in range(n):
        if i!=0:
            for j in range(8):
                for k in range(8):
                    if bitcheck[j][k]:
                        dp[i][k]=min(dp[i][k],dp[i-1][j]+bitcalc[b[i][0]+b[i][1]*2+b[i][2]*4][k])
        else:
            for k in range(8):
                dp[i][k]=bitcalc[b[i][0]+b[i][1]*2+b[i][2]*4][k]
    print(min(dp[n-1]))
    exit()