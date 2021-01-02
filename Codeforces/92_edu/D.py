t=int(input())
def solve3(n,k,l1,r1,l2,r2):
    A,B=l2-r1,r2-l1
    #ギリギリまで何個ぶん埋めれるか
    g=min(n,k//B)
    ans=g*(A+B)
    k-=g*B
    #残りのk(Bより小さい)を1/2使うのか1まで頑張るか
    if g==n:
        #gがnの時はさらにもう一つは無理
        ans=ans+2*k
    else:
        ans=min(ans+A+k,ans+2*k)
    print(ans)

def solve1(n,k,l1,r1,l2,r2):
    A,B=l2-r1,r2-l1
    #何個ぶん1までいくか
    ans=100000000000000
    for i in range(1,n+1):
        ans_=i*A
        if k<=i*B:
            ans=min(ans,ans_+k)
        else:
            ans=min(ans,ans_+i*B+(k-i*B)*2)
    print(ans)

def solve2(n,k,l1,r1,l2,r2):
    X=abs(l1-l2)+abs(r1-r2)
    if r2<r1:
        k-=(r2-l2)*n
    else:
        k-=(r1-l2)*n
    if k<=X*n:
        print(max(k,0))
    else:
        #1/2を含む
        ans=X*n
        k-=X*n
        print(ans+2*k)

for _ in range(t):
    n,k=map(int,input().split())
    l1,r1=map(int,input().split())
    l2,r2=map(int,input().split())
    if l1>l2:
        l1,l2=l2,l1
        r1,r2=r2,r1
    if l2>=r1:
        solve1(n,k,l1,r1,l2,r2)
    else:
        solve2(n,k,l1,r1,l2,r2)