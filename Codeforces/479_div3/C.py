n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
if k==0:
    if a[0]==1:
        print(-1)
    else:
        print(a[0]-1)
elif k==n:
    print(a[-1])
else:
    if a[k-1]==a[k]:
        print(-1)
    else:
        print(a[k-1])