from collections import Counter
n,m=map(int,input().split())
d=Counter(list(map(int,input().split())))
for i in range(m):
    b,c=map(int,input().split())
    if c in d:
        d[c]+=b
    else:
        d[c]=b
d=sorted(Counter(d).items(),reverse=True)
check=n
ans=0
for i in d:
    if i[1]<check:
        check-=i[1]
        ans+=(i[0]*i[1])
    else:
        ans+=(i[0]*check)
        print(ans)
        break