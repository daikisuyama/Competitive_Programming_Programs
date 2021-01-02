#https://atcoder.jp/contests/joi2020yo2/tasks/joi2020_yo2_c
def check(n):
    ret=0
    while n!=0:
        ret+=(n%10)
        n//=10
    return ret
n=int(input())
dp=[1]*n
for i in range(n):
    c=check(i+1)
    if i+c<n:
        dp[i+c]+=dp[i]
print(dp[n-1])