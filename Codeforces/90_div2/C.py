from itertools import accumulate
for _ in range(int(input())):
    s=input()
    l=len(s)
    t=[1 if s[i]=="+" else -1 for i in range(l)]
    t=list(accumulate(t))
    now=0
    ans=0
    for i in range(l):
        if t[i]<now:
            ans+=(i+1)
            now=t[i]
        if i==l-1:
            ans+=(i+1)
    print(ans)