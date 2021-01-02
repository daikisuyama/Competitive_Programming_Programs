s=input()
t=input()
ans=0
for i in range(len(s)):
    ans+=(s[i]!=t[i])
print(ans)