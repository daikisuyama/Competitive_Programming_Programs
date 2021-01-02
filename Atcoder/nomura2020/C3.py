from itertools import accumulate
n=int(input())
a=list(map(int,input().split()))
c=list(accumulate(a))
b=[0]*(n+1)
#大きくしすぎてしまう場合がある
#いや上限を考えろや
def f():
    global n,a,b
    for i in range(n+1):
        if i==0:
            b[0]=min(c[n]-c[0],1)
        else:
            b[i]=min(2*(b[i-1]-a[i-1]),c[n]-c[i-1])

    if n==0:
        if a[0]!=1:
            print(-1)
        else:
            print(1)
    elif b[n]!=a[n]:
        print(-1)
    else:
        print(sum(b))
        #print(b)
f()