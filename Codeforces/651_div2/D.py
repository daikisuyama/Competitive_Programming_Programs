#片方都合よく選べる
n,k=map(int,input().split())
a=list(map(int,input().split()))
def f(x):
    global n,k,a
    #x以下にできるか(こっちは奇数番目)
    check=0
    now=1
    for i in range(n):
        if now:
            if a[i]<=x:
                now=1-now
                check+=1
        else:
            now=1-now
            check+=1
    if check>=k:
        #print(check)
        return True
    #偶数番目
    check=0
    now=0
    for i in range(n):
        if now:
            if a[i]<=x:
                now=1-now
                check+=1
        else:
            now=1-now
            check+=1
    if check>=k:
        #print(check)
        return True
    else:
        #print(check)
        return False
l,r=0,10**9+1
#最小値を求める
while l+1<r:
    m=l+(r-l)//2
    #print(f(m))
    if f(m):
        r=m
    else:
        l=m
print(r)


