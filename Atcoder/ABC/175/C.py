x,k,d=map(int,input().split())
x=abs(x)
if x>k*d:
    print(x-k*d)
else:
    k-=x//d
    x-=(d*(x//d))
    ans=[x,abs(d-x)]
    print(ans[k%2])