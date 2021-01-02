import heapq
x,y,a,b,c=map(int,input().split())
def _int(x):
    return -int(x)
p=list(map(_int,input().split()))
q=list(map(_int,input().split()))
r=list(map(_int,input().split()))
heapq.heapify(p)
heapq.heapify(q)
heapq.heapify(r)

ans=[]
heapq.heapify(ans)
for i in range(x):
    _p=heapq.heappop(p)
    heapq.heappush(ans,-_p)
for i in range(y):
    _q=heapq.heappop(q)
    heapq.heappush(ans,-_q)
#ansは小さい順、rは大きい順
for i in range(x+y):
    if len(r)==0:break
    _ans=heapq.heappop(ans)
    _r=-heapq.heappop(r)
    if _r>=_ans:
        heapq.heappush(ans,_r)
    else:
        heapq.heappush(ans,_ans)
        break
print(sum(ans))