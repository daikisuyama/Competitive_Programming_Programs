def f(x):
    global n,k
    q=p
    q-=sum(a[:x])
    if q<0:
        return 0
    ret=x
    for i in range((n-x)//k):
        if a[x-1+(i+1)*k]<=q:
            ret+=k
            q-=a[x-1+(i+1)*k]
        else:
            break
    return ret

for _ in range(int(input())):
    n,p,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    cand=[0]*k
    for i in range(k):
        cand[i]=f(i)
    print(max(cand))