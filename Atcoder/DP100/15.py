n=int(input())
s=input()
l=len(s)
t=[]
for i in range(n):
    t_=input()
    t.append([t_,len(t_)])
mod=10**9+7
dp=[0]*l
for i in range(n):
    if s[0:t[i][1]]==t[i][0]:
        dp[t[i][1]-1]=1
for i in range(l):
    for j in range(n):
        if s[i+1:i+t[j][1]+1]==t[j][0]:
            dp[i+t[j][1]]+=dp[i]
            dp[i+t[j][1]]%=mod
print(dp[l-1])