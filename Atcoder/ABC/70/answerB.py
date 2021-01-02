a,b,c,d=map(int,input().split())
k,l=max(a,c),min(b,d)

if k>=l:
    print(0)
else:
    print(l-k)
