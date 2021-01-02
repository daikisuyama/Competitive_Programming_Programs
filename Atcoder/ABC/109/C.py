from fractions import gcd
n,X=map(int,input().split())
x=list(map(int,input().split()))

def hoge():
    global n,x,X
    ret=abs(X-x[0])
    for i in range(1,n):
        ret=gcd(abs(X-x[i]),ret)
    return ret

print(hoge())