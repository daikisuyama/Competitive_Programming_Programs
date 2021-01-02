from sys import setrecursionlimit
setrecursionlimit(10**7)
s,t=input(),input()
dp=[[0]*(len(t)+1) for i in range(len(s)+1)]
for i in range(len(s)+1):
    for j in range(len(t)+1):
        if i<len(s):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])
        if j<len(t):
            dp[i][j+1]=max(dp[i][j+1],dp[i][j])
        if i<len(s) and j<len(t):
            dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+(s[i]==t[j]))
ans=""
def move(i,j):
    global dp,ans
    if i==0 or j==0:
        return
    elif dp[i][j]>dp[i-1][j-1] and s[i-1]==t[j-1]:
        ans=s[i-1]+ans
        move(i-1,j-1)
    else:
        if dp[i][j]==dp[i][j-1]:
            move(i,j-1)
        else:
            move(i-1,j)
move(len(s),len(t))
print(ans)