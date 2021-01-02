n=int(input())
a=list(map(int,input().split()))
#大きくしすぎてしまう場合がある
def f():
    global n,a
    node_num,now=0,0
    for i in range(n,-1,-1):
        if n<=100:
            now_=now
            now=min(now+a[i],2**i)
        else:
            now_=now
            now=now+a[i]
        node_num+=now
        if now<-(-now_//2):
            print(-1)
            break
        print(now)
    else:
        print(node_num)
f()