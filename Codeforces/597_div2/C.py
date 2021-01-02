mod=10**9+7
s=input()
n=len(s)
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    dp[i]+=dp[i-1]
    dp[i]%=mod
    #print(s[i-2:i])
    if s[i-2:i]=="uu" or s[i-2:i]=="nn":
        dp[i]+=dp[i-2]
        dp[i]%=mod
#print(dp)
if ("w" in s)or("m" in s):
    print(0)
else:
    print(dp[n])