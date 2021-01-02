n,k=map(int,input().split())
h=[int(i) for i in input().split()]
h.sort(reverse=True)

if k>=n:
    print(0)
else:
    print(sum(h[k:]))
