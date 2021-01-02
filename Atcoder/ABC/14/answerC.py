import sys
#input→sys.stdin.readline3/4の時間に
input=sys.stdin.readline
n=int(input())
x=[0]*1000001
for i in range(n):
    a,b=map(int,input().split())
    x[a]+=1
    if b+1<1000001:
        x[b+1]-=1
ans=x[0]
for i in range(1000000):
    x[i+1]+=x[i]
    ans=max(ans,x[i+1])
print(ans)
