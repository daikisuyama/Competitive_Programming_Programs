#11/26 16:20~22
a,b,k=map(int,input().split())
if k>=a+b:
    print(0,0)
elif k>a:
    print(0,b-(k-a))
else:
    print(a-k,b)