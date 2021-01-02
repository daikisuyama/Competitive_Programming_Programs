n=int(input())
a=list(map(int,input().split()))
#大きくしすぎてしまう場合がある
def f():
    global n,a
    node_num,now=0,1
    for i in range(n+1):
        if i==0:
            node_num+=1
        else:
            node_num+=now
        now-=a[i]
        now*=2
        if now<0:
            return -1
    else:
        if now==0:
            return -1
        else:
            return node_num

l,r=0,10**20
while l+1<r:
    k=l+(r-l)//2
    if f()>=0:
        r=k
    else:
        l=k
