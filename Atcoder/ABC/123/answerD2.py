#AC済み
import heapq
x,y,z,k=map(int,input().split())
#heapqは小さい順にしか並べられないので、-をつければ大きい順になる
a=sorted([-int(i) for i in input().split()])
b=sorted([-int(i) for i in input().split()])
c=sorted([-int(i) for i in input().split()])
check=set()
ans=[]
heapq.heappush(ans,(a[0]+b[0]+c[0],0,0,0))
check.add((0,0,0))
for i in range(k):
    h=heapq.heappop(ans)
    print(-h[0])
    if h[1]+1<x:
        if (h[1]+1,h[2],h[3]) not in check:
            heapq.heappush(ans,(a[h[1]+1]+b[h[2]]+c[h[3]],h[1]+1,h[2],h[3]))
            check.add((h[1]+1,h[2],h[3]))
    if h[2]+1<y:
        if (h[1],h[2]+1,h[3]) not in check:
            heapq.heappush(ans,(a[h[1]]+b[h[2]+1]+c[h[3]],h[1],h[2]+1,h[3]))
            check.add((h[1],h[2]+1,h[3]))
    if h[3]+1<z:
        if (h[1],h[2],h[3]+1) not in check:
            heapq.heappush(ans,(a[h[1]]+b[h[2]]+c[h[3]+1],h[1],h[2],h[3]+1))
            check.add((h[1],h[2],h[3]+1))
