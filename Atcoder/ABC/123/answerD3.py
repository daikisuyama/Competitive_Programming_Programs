import heapq
x,y,z,k=map(int,input().split())
a=sorted([int(i) for i in input().split()],reverse=True)
b=sorted([int(i) for i in input().split()],reverse=True)
c=sorted([int(i) for i in input().split()],reverse=True)

def solve(p):
    cnt=0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if a[i]+b[j]+c[k]>=p:
                    cnt+=1
                    if cnt>=k:
                        return True
                else:
                    break
    return False

l,r=0,a[0]+b[0]+c[0]
while r>l+1:
    t=(l+r)//2
    if solve(t):
        r=t
    else:
        l=t
ans=[]
for i in range(x):
    for j in range(y):
        for m in range(z):
            if a[i]+b[j]+c[m]>=r:
                heapq.heappush(ans,-(a[i]+b[j]+c[m]))
            else:
                break
for i in range(k):
    print(-heapq.heappop(ans))
