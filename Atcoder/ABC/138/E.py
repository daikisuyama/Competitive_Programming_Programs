from bisect import bisect_right
s=input()
t=input()
ns=len(s)
nt=len(t)
alp=[[] for i in range(26)]
for i in range(ns):
    alp[ord(s[i])-97].append(i)
alpl=[len(alp[i]) for i in range(26)]
ans=0
now=-1
for i in range(nt):
    if alpl[ord(t[i])-97]==0:
        exit(print(-1))
    b=bisect_right(alp[ord(t[i])-97],now)
    if b==alpl[ord(t[i])-97]:
        now=alp[ord(t[i])-97][0]
        ans+=ns
        if i==nt-1:
            ans+=(now+1)
    else:
        now=alp[ord(t[i])-97][b]
        if i==nt-1:
            ans+=(now+1)
print(ans)