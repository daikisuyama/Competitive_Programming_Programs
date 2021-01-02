import sys
input=sys.stdin.readline
n,a,b,c=map(int,input().split())
s=[input() for i in range(n)]
dp=[dict() for i in range(n+1)]
dp[0][(a,b,c)]=""
for i in range(n):
    if len(dp[i])==0:
        print("No")
        break
    if s[i][0]=="A" and s[i][1]=="B":
        #print(0)
        for j in dp[i]:
            a,b,c=j
            if a>0:
                dp[i+1][(a-1,b+1,c)]=dp[i][j]+"B"
            if b>0:
                dp[i+1][(a+1,b-1,c)]=dp[i][j]+"A"
    elif s[i][0]=="A" and s[i][1]=="C":
        #print(1)
        for j in dp[i]:
            a,b,c=j
            if a>0:
                dp[i+1][(a-1,b,c+1)]=dp[i][j]+"C"
            if c>0:
                dp[i+1][(a+1,b,c-1)]=dp[i][j]+"A"
    else:
        #print(2)
        for j in dp[i]:
            a,b,c=j
            if b>0:
                dp[i+1][(a,b-1,c+1)]=dp[i][j]+"C"
            if c>0:
                dp[i+1][(a,b+1,c-1)]=dp[i][j]+"B"
else:
    if len(dp[n])==0:
        print("No")
    else:
        print("Yes")
        #print(dp)
        z=list(dp[n].items())
        #print(z)
        for i in range(n):
            print(z[0][1][i])




