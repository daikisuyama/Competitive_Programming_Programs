q=int(input())
def check(t,a,b):
    k=(2*a+t)//2
    return k*(2*a+t-k)<a*b

for i in range(q):
    a,b=sorted(map(int,input().split()))
    if a==b or a==b-1:
        print(2*a-2)
        continue
    l,r=1,b-a
    while l+1<r:
        t=(l+r)//2
        if check(t,a,b):
            l=t
        else:
            r=t
    if check(r,a,b):
        print(2*a-2+r)
    else:
        print(2*a-2+l)