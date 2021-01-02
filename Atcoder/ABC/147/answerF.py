n,x,d=map(int,input().split())
k=(2*x+(n-1)*d)*n
#print(k)
k-=(2*x)
if k==0:
    print(2)
else:
    k-=(2*20)
    if k==0:
        print(3)
    else:
        print(3+k//(2*2))
