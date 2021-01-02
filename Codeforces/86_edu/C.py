from itertools import accumulate
def f(i):
    global a,b,pre
    x=i//(a*b)
    y=i%(a*b)
    return x*pre[-1]+pre[y]
for _ in range(int(input())):
    a,b,q=map(int,input().split())
    pre=[int((i%a)%b!=(i%b)%a) for i in range(a*b)]
    pre=list(accumulate(pre))
    ans=[]
    for i in range(q):
        l,r=map(int,input().split())
        ans.append(str(f(r)-f(l-1)))
        #print(f(r),f(l-1))
    print(" ".join(map(str,ans)))