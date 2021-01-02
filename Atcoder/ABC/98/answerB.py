n=int(input())
s=input()
ans=0
for i in range(n-1):
    s1=s[:i+1]
    s2=s[i+1:]
    s3=set(s1)&set(s2)
    ans=max(ans,len(s3))
print(ans)