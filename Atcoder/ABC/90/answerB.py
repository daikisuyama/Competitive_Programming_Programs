a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    s=str(i)
    l=len(s)
    for i in range(l//2):
        if s[i]!=s[l-1-i]:
            break
    else:
        ans+=1
print(ans)