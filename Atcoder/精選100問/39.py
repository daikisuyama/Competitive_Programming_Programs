#14:18
#O(n)\times 20
n=int(input())
a=list(map(int,input().split()))
#dp[i][j](i,j)での候補
dp=[[0]*21 for i in range(n-1)]
dp[0][a[0]]=1
for i in range(n-2):
    for j in range(21):
        if j+a[i+1]<=20:
            dp[i+1][j+a[i+1]]+=dp[i][j]
        if j-a[i+1]>=0:
            dp[i+1][j-a[i+1]]+=dp[i][j]
print(dp[n-2][a[n-1]])
