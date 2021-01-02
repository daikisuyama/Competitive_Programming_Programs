import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    q=list(map(int,input().split()))
    p=[-1]*n
    p[0]=q[0]
    check=[0]*n
    check[p[0]-1]=1
    now=0 if p[0]!=1 else 1
    for i in range(1,n):
        if q[i]!=q[i-1]:
            if check[q[i]-1]:
                print(-1)
                break
            else:
                check[q[i]-1]=1
                p[i]=q[i]
        else:
            while True:
                if not check[now]:
                    check[now]=1
                    p[i]=now+1
                    break
                now+=1
            if q[i]<p[i]:
                print(-1)
                break
    else:
        print(" ".join(map(str,p)))
                    