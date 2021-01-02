from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=sorted(input())
    t=list(Counter(s).items())
    if len(t)==1:
        print(s[0]*(-(-n//k)))
        continue
    now=s[0]
    ans=s[k-1]
    if now!=ans:
        print("".join(ans))
    elif len(t)>=3:
        print("".join(s[k-1:]))
    elif t[0][1]==k:
        print(t[0][0]+t[1][0]*(-(-n//k)-1))
    else:
        print("".join(s[k-1:]))