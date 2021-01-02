#常に貪欲に選べない、順番などを考慮しなきゃいけない場合はdp、アホか
n=int(input())
a=[int(i) for i in input().split()]
dp=[10000000000000]*n
dp[0]=0
for i in range(n):
    if i<n-1:
        dp[i+1]=min(dp[i]+abs(a[i+1]-a[i]),dp[i+1])
    if i<n-2:
        dp[i+2]=min(dp[i]+abs(a[i+2]-a[i]),dp[i+2])
print(dp[-1])
