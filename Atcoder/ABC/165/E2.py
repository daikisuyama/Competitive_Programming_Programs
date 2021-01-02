n,m=map(int,input().split())
if n%2==1:
    l=n//2
    for i in range(m):
        if i%2==1:
            print(i//2+1,l-i//2)
        else:
            print(l+i//2+1,n-i//2)
else:
    l=n//2
    for i in range(m):
        if i%2==0:
            print(i//2+1,l-i//2)
        else:
            print(l+i//2+2,n-i//2)

