n=int(input())
s=[input() for i in range(n)]
m=int(input())
t=[input() for i in range(m)]
s2=dict()
t2=dict()
for i in range(n):
    if s[i] in s2:
        s2[s[i]]+=1
    else:
        s2[s[i]]=1
        t2[s[i]]=0
for i in range(m):
    if t[i] in t2:
        t2[t[i]]+=1
    else:
        t2[t[i]]=1
ans=0
for i in s2:
    ans=max(s2[i]-t2[i],ans)
print(ans)
